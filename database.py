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