from datetime import datetime

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import TOKEN
import states
import database

usuarios = {}
solicitudes = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.message.chat_id

    usuarios[usuario] = states.ESPERANDO_DNI

    await update.message.reply_text(
        "Bienvenido al sistema de gestión de vacaciones.\n\nIngrese su DNI:"
    )

async def mensajes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.message.chat_id
    texto = update.message.text

    estado = usuarios.get(usuario)

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
                "Empleado no encontrado."
            )
            return

        solicitudes[usuario] = {
            "DNI": texto,
            "Nombre": empleado["Nombre"],
            "Saldo": empleado["Saldo"]
        }

        usuarios[usuario] = states.ESPERANDO_FECHA

        await update.message.reply_text(
            f"Hola {empleado['Nombre']}.\n"
            f"Saldo disponible: {empleado['Saldo']} días.\n\n"
            f"Ingrese la fecha de inicio:"
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
                "Fecha inválida.\nUse formato dd/mm/aaaa"
            )

            return


        solicitudes[usuario]["Fecha"] = texto

        usuarios[usuario] = states.ESPERANDO_DIAS

        await update.message.reply_text(
            "Ingrese la cantidad de días:"
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
                "No posee saldo suficiente."
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
            "Pendiente"
            }

        database.guardar_solicitud(solicitud)

        await update.message.reply_text(
            "Solicitud registrada correctamente."
        )

        usuarios.pop(usuario)


def main():

    print("Iniciando aplicación...")

    app = Application.builder().token(TOKEN).build()

    print("Aplicación creada")

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            mensajes
        )
    )

    print("Bot funcionando...")

    app.run_polling()


if __name__ == "__main__":
    main()