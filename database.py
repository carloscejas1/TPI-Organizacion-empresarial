import pandas as pd

ARCHIVO_EMPLEADOS = "data/empleados.xlsx"
ARCHIVO_SOLICITUDES = "data/solicitudes.xlsx"


def buscar_empleado(dni):

    empleados = pd.read_excel(ARCHIVO_EMPLEADOS)

    resultado = empleados[
        empleados["DNI"] == int(dni)
    ]

    if len(resultado) > 0:
        return resultado.iloc[0]

    return None


def guardar_solicitud(datos):

    try:
        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

    except:
        solicitudes = pd.DataFrame()

    solicitudes = pd.concat(
        [
            solicitudes,
            pd.DataFrame([datos])
        ],
        ignore_index=True
    )

    solicitudes.to_excel(
        ARCHIVO_SOLICITUDES,
        index=False
    )

def obtener_siguiente_id():

    try:

        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

        if solicitudes.empty:
            return 1

        if "ID" not in solicitudes.columns:
            return 1

        ids = solicitudes["ID"].dropna()

        if ids.empty:
            return 1

        return int(ids.max()) + 1

    except:

        return 1
    
def obtener_solicitudes(dni):

    try:

        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

        return solicitudes[
            solicitudes["DNI"] == int(dni)
        ]

    except:

        return pd.DataFrame()
    
def aprobar_solicitud(id_solicitud):

    solicitudes = pd.read_excel(
        ARCHIVO_SOLICITUDES
    )

    solicitudes.loc[
        solicitudes["ID"] == id_solicitud,
        "Estado"
    ] = "Aprobada"

    solicitudes.to_excel(
        ARCHIVO_SOLICITUDES,
        index=False
    )

def rechazar_solicitud(id_solicitud):

    solicitudes = pd.read_excel(
        ARCHIVO_SOLICITUDES
    )

    solicitudes.loc[
        solicitudes["ID"] == id_solicitud,
        "Estado"
    ] = "Rechazada"

    solicitudes.to_excel(
        ARCHIVO_SOLICITUDES,
        index=False
    )

def existe_solicitud(id_solicitud):

    try:

        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

        return (
            solicitudes["ID"] == id_solicitud
        ).any()

    except:

        return False
    
def obtener_estado_solicitud(id_solicitud):

    try:

        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

        resultado = solicitudes[
            solicitudes["ID"] == id_solicitud
        ]

        if len(resultado) == 0:
            return None

        return resultado.iloc[0]["Estado"]

    except:

        return None
    
def dias_pendientes(dni):

    try:

        solicitudes = pd.read_excel(
            ARCHIVO_SOLICITUDES
        )

        resultado = solicitudes[
            (solicitudes["DNI"] == int(dni))
            &
            (solicitudes["Estado"] == "Pendiente")
        ]

        return resultado["Dias"].sum()

    except:

        return 0