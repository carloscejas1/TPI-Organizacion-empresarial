# GESTIÓN DE VACACIONES - CHATBOT TELEGRAM

Descripción

Este proyecto corresponde al Trabajo Práctico Integrador de la materia Organización Empresarial de la Tecnicatura Universitaria en Programación.

La solución propuesta automatiza el proceso administrativo de solicitud de vacaciones mediante un chatbot desarrollado para Telegram.

El objetivo es reemplazar tareas manuales por un flujo automatizado que permita:

* Consultar saldo de vacaciones.
* Solicitar días de licencia.
* Validar reglas de negocio.
* Registrar solicitudes.
* Simular aprobación o rechazo.

Tecnologías Utilizadas

* Python
* Telegram Bot API
* Pandas
* OpenPyXL
* GitHub
* BPMN 2.0

Estructura del Proyecto

```text
TPI-Organizacion-empresarial/
```

Contiene:

* Código fuente
* Diagramas BPMN
* Base de datos simulada
* Documentación
* Casos de prueba

Proceso Automatizado

1. El empleado inicia conversación con el bot.
2. El bot solicita identificación.
3. Consulta el saldo disponible.
4. Solicita fechas y cantidad de días.
5. Verifica reglas de negocio.
6. Simula aprobación.
7. Registra la solicitud.
8. Notifica el resultado.

Base de Datos

La persistencia se simula mediante archivos Excel:

* empleados.xlsx
* solicitudes.xlsx

Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
```

Autores

* Carlos Cejas
* Agustín Atminis

Materia

Organización Empresarial

Tecnicatura Universitaria en Programación
UTN
