from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

import states
import database

from config import ADMIN_IDS

usuarios = {}
solicitudes = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.message.chat_id

    usuarios[usuario] = states.ESPERANDO_DNI

    await update.message.reply_text(
        "Bienvenido al sistema de gestión de vacaciones.\n Ingresá tu número de documento: "
    )

async def consultar(update: Update,
                    context: ContextTypes.DEFAULT_TYPE):

    usuario = update.message.chat_id

    usuarios[usuario] = (
        states.CONSULTANDO_SOLICITUDES
    )

    await update.message.reply_text(
        "Ingrese su DNI para consultar solicitudes:"
    )

async def mensajes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.message.chat_id
    texto = update.message.text

    estado = usuarios.get(usuario)

    if estado == states.CONSULTANDO_SOLICITUDES:

        solicitudes_usuario = (
            database.obtener_solicitudes(texto)
            )

        if solicitudes_usuario.empty:

            await update.message.reply_text(
                "No se encontraron solicitudes."
            )

            usuarios.pop(usuario)

            return

        respuesta = ""

        for _, fila in solicitudes_usuario.iterrows():

            respuesta += (
                f"Solicitud #{fila['ID']}\n"
                f"Fecha: {fila['FechaInicio']}\n"
                f"Días: {fila['Dias']}\n"
                f"Estado: {fila['Estado']}\n\n"
            )

        await update.message.reply_text(
            respuesta
        )

        usuarios.pop(usuario)

        return

    # Estado: esperando DNI
    if estado == states.ESPERANDO_DNI:

        try:
            empleado = database.buscar_empleado(texto)
        except:
            await update.message.reply_text(
                "Debe ingresar un DNI numérico."
            )
            return

        if empleado is None:
            await update.message.reply_text(
                "No encontré ese DNI en el sistema. Verificá el número e intentá de nuevo."
            )
            return

        saldo_original = empleado["Saldo"]

        dias_reservados = database.dias_pendientes(texto)

        saldo_disponible = (
            saldo_original
            - dias_reservados
            )

        solicitudes[usuario] = {
            "DNI": texto,
            "Nombre": empleado["Nombre"],
            "Saldo": saldo_disponible
            }

        usuarios[usuario] = states.ESPERANDO_FECHA

        await update.message.reply_text(
            f"Hola {empleado['Nombre']}.\n"
            f"Tenés {saldo_disponible} días disponibles.\n"
            f"Ingresá la fecha de inicio:"
            )

    # Estado: esperando fecha
    elif estado == states.ESPERANDO_FECHA:

        try:
            fecha = datetime.strptime(
                texto,
                "%d/%m/%Y"
            )

        except ValueError:

            await update.message.reply_text(
                "Formato de fecha incorrecto. \nIngresá la fecha así: DD/MM/AAAA."
            )

            return


        solicitudes[usuario]["Fecha"] = texto

        usuarios[usuario] = states.ESPERANDO_DIAS

        await update.message.reply_text(
            "Ingrese la cantidad de días: "
        )

    # Estado: esperando días
    elif estado == states.ESPERANDO_DIAS:

        try:
            dias = int(texto)
        except:
            await update.message.reply_text(
                "Ingrese un número válido."
            )
            return

        saldo = solicitudes[usuario]["Saldo"]

        if dias > saldo:

            await update.message.reply_text(
                "Solicitás más días de los que tenés disponibles. Elegí un período más corto. "
            )

            usuarios.pop(usuario)

            return

        solicitud = {
            "ID":
            database.obtener_siguiente_id(),

            "DNI":
            solicitudes[usuario]["DNI"],

            "FechaInicio":
            solicitudes[usuario]["Fecha"],

            "Dias":
            dias,

            "Estado":
            "Pendiente",

            "FechaSolicitud": 
            datetime.now().strftime("%d/%m/%Y")
            }

        database.guardar_solicitud(solicitud)

        await update.message.reply_text(
            "Solicitud registrada correctamente."
        )

        usuarios.pop(usuario)

async def aprobar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.chat_id not in ADMIN_IDS:
        await update.message.reply_text("No tiene permisos para realizar esta acción.")
        return

    try:

        id_solicitud = int(
            context.args[0]
        )

    except:

        await update.message.reply_text(
            "Uso: /aprobar ID"
        )

        return

    if not database.existe_solicitud(id_solicitud):
        await update.message.reply_text("Solicitud no encontrada.")
        return
    
    estado_actual = (database.obtener_estado_solicitud(id_solicitud))

    if estado_actual == "Aprobada":
        await update.message.reply_text("La solicitud ya se encuentra aprobada.")
        return
    
    if estado_actual == "Rechazada":
        await update.message.reply_text("No es posible aprobar una solicitud rechazada.")
        return

    database.aprobar_solicitud(id_solicitud)

    await update.message.reply_text(
        f"Solicitud {id_solicitud} aprobada.")

async def rechazar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.chat_id not in ADMIN_IDS:
        await update.message.reply_text(
        "No tiene permisos para realizar esta acción.")
        return

    try:

        id_solicitud = int(
            context.args[0]
        )

    except:

        await update.message.reply_text(
            "Uso: /rechazar ID"
        )

        return

    if not database.existe_solicitud(id_solicitud):
        await update.message.reply_text("Solicitud no encontrada.")
        return
    
    estado_actual = (database.obtener_estado_solicitud(id_solicitud))

    if estado_actual == "Rechazada":
        await update.message.reply_text("La solicitud ya se encuentra rechazada.")
        return
    
    if estado_actual == "Aprobada":
        await update.message.reply_text("No es posible rechazar una solicitud aprobada.")
        return

    database.rechazar_solicitud(id_solicitud)

    await update.message.reply_text(
        f"Solicitud {id_solicitud} rechazada."
        )

async def ayuda(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    mensaje = """
📋 Sistema de Gestión de Vacaciones

Comandos disponibles:

/start
Solicitar vacaciones

/consultar
Consultar solicitudes por DNI

/aprobar ID
Aprobar una solicitud

/rechazar ID
Rechazar una solicitud

/ayuda
Mostrar esta ayuda

Desarrollado para el Trabajo Integrador de Organización Empresarial.
Versión 1.0
"""

    await update.message.reply_text(
        mensaje
    )