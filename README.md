# 🤖 GESTIÓN DE VACACIONES - CHATBOT TELEGRAM

## 📌 Trabajo Práctico Integrador - Organización Empresarial

Proyecto desarrollado para la materia **Organización Empresarial** de la **Tecnicatura Universitaria en Programación (TUP)**.

El objetivo es automatizar el proceso administrativo de **Gestión de Vacaciones** mediante un chatbot implementado sobre la plataforma **Telegram**, modelando previamente el proceso utilizando la metodología **BPMN 2.0**.

---

## 👥 Integrantes

* Carlos Cejas
* Agustín Atminis
---

## 🎯 Objetivo

Diseñar una solución tecnológica capaz de automatizar el proceso de solicitud de vacaciones dentro de una organización, permitiendo:

* Registrar solicitudes de vacaciones.
* Consultar solicitudes realizadas.
* Validar reglas de negocio.
* Aprobar o rechazar solicitudes.
* Gestionar permisos de acceso para RRHH.
* Mantener trazabilidad de las solicitudes.

---

## 🏢 Organización Analizada

**Empresa ficticia:** TechSolutions S.A.

### Situación Actual (AS-IS)

Actualmente las solicitudes de vacaciones se realizan de forma manual mediante correos electrónicos y mensajes internos.

Problemas detectados:

* Demoras en la aprobación.
* Errores en el cálculo de días disponibles.
* Falta de trazabilidad.
* Exceso de tareas administrativas para RRHH.

### Situación Propuesta (TO-BE)

Se implementa un chatbot de Telegram que automatiza el proceso de punta a punta, reduciendo tiempos y mejorando la gestión de la información.

---

## 📊 BPMN 2.0

### Proceso AS-IS

Diagrama que representa el proceso actual de gestión de vacaciones.

Ubicación:

```text
docs/BMPN-AS-IS.svg
```

### Proceso TO-BE

Diagrama que representa el proceso automatizado mediante chatbot.

Ubicación:

```text
docs/BPMN-TO-BE.svg
```

---

## ✅ Funcionalidades Implementadas

- Registro de solicitudes de vacaciones.
- Consulta de solicitudes por DNI.
- Validación de saldo disponible.
- Validación de formato de fecha.
- Generación automática de ID.
- Aprobación de solicitudes.
- Rechazo de solicitudes.
- Control de permisos mediante chat_id.
- Persistencia de datos en Excel.
- Sistema de ayuda integrado.

---

## 🛠 Tecnologías Utilizadas

* Python 3
* Telegram Bot API
* Pandas
* OpenPyXL
* Git
* GitHub
* BPMN 2.0

---

## 📂 Estructura del Proyecto

```text
TPI-Organizacion-empresarial/
│
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── database.py
├── states.py
├── handlers.py
│
├── data/
│   ├── empleados.xlsx
│   └── solicitudes.xlsx
│
├── docs/
    ├── BMPN-AS-IS.svg
    ├── BPMN-TO-BE.svg
    ├── Presentación-TPI-OE.pdf
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/carloscejas1/TPI-Organizacion-empresarial.git
```

### 2. Ingresar al proyecto

```bash
cd TPI-Organizacion-empresarial
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear token de bot con @botfather
En Telegram ir a @botfather
```
/start
/newbot
Ingresar nombre y usuario de bot
```

### 4. Crear .env
En la raiz del repositorio crear un archivo .env 
e ingresar las siguientes variables:
```
TOKEN = "token_de_botfather"

ADMIN_ID = ID_Telegram
```
El id de administrador es necesario para aprobar
las solicitudes y se obtiene con el bot @userinfo

---

## ▶️ Ejecución

```bash
python main.py
```
Con el programa en ejecución ingresar a Telegram
con el @bot-id y utilizar el bot.

---

## 🗄 Persistencia de Datos

La persistencia se realiza mediante archivos Excel.

### empleados.xlsx

Contiene:

* DNI
* Nombre
* Saldo de vacaciones disponible

### solicitudes.xlsx

Contiene:

- ID
- DNI
- FechaInicio
- Dias
- Estado
- FechaSolicitud

## 🔄 Máquina de Estados

El chatbot utiliza una máquina de estados para mantener el contexto de cada usuario.

Estados principales:

```text
ESPERANDO_DNI
ESPERANDO_FECHA
ESPERANDO_DIAS
CONSULTANDO_SOLICITUDES
```

---

## 🌳 Flujo del Proceso

1. El empleado inicia la solicitud.
2. El sistema valida el DNI.
3. El sistema muestra el saldo disponible de vacaciones.
4. Se solicita fecha de inicio.
5. Se solicita cantidad de días.
6. Se valida disponibilidad.
7. Se registra la solicitud con estado "Pendiente".
8. RRHH puede aprobar o rechazar la solicitud.
9. El empleado puede consultar el estado de sus solicitudes.

## 🤖 Comandos Disponibles

| Comando | Descripción |
|----------|------------|
| /start | Iniciar solicitud de vacaciones |
| /consultar | Consultar solicitudes por DNI |
| /aprobar ID | Aprobar solicitud (solo administradores) |
| /rechazar ID | Rechazar solicitud (solo administradores) |
| /ayuda | Mostrar ayuda |

## 🔐 Control de Acceso

Las acciones de aprobación y rechazo están restringidas a usuarios autorizados mediante la validación del chat_id de Telegram.

Solo los administradores definidos en la configuración pueden ejecutar:

- /aprobar ID
- /rechazar ID

## 🚦 Gateways (Decisiones BPMN)

### Gateway 1

¿Posee saldo suficiente?

* Sí → continúa proceso.
* No → rechaza solicitud.

### Gateway 2

¿Supervisor aprueba?

* Sí → solicitud aprobada.
* No → solicitud rechazada.

---

## ❌ Manejo de Errores (Camino Infeliz)

El sistema contempla:

### DNI inválido

```text
Debe ingresar un DNI válido.
```

### Empleado inexistente

```text
Empleado no encontrado.
```

### Cantidad de días incorrecta

```text
Ingrese un número válido.
```

### Saldo insuficiente

```text
No posee días suficientes para realizar la solicitud.
```

### Fecha inválida

```text
Ingrese una fecha válida.
```

---

## 🤖 Uso de Inteligencia Artificial

Para el desarrollo del proyecto se utilizaron herramientas de IA como apoyo para:

* Diseño de BPMN.
* Generación de documentación.
* Diseño de casos de prueba.
* Asistencia en programación Python.

## 📚 Documentación

### Manual de Usuario

```docs/Presentación-TPI-OE.pdf

## 📄 Licencia

Proyecto desarrollado exclusivamente con fines académicos para la materia Organización Empresarial.

---

## 🎓 Universidad

**Tecnicatura Universitaria en Programación**

**Organización Empresarial**

**Trabajo Práctico Integrador**
