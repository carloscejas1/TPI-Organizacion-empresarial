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

* Consultar saldo disponible de vacaciones.
* Solicitar días de licencia.
* Validar reglas de negocio.
* Simular aprobación o rechazo.
* Registrar solicitudes.
* Notificar resultados al empleado.

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
docs/BPMN_AS_IS.png
```

### Proceso TO-BE

Diagrama que representa el proceso automatizado mediante chatbot.

Ubicación:

```text
docs/BPMN_TO_BE.png
```

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
│   ├── BPMN_AS_IS.png
│   ├── BPMN_TO_BE.png
│   ├── diccionario_datos.pdf
│   ├── manual_usuario.pdf
│   └── capturas_IA/
│       └── .gitkeep
│
├── tests/
│   ├── test_saldo.py
│   ├── test_solicitudes.py
│   └── test_errores.py
│
└── screenshots/
    ├── bot_funcionando.png
    └── github_repo.png
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/usuario/TPI-Organizacion-empresarial.git
```

### 2. Ingresar al proyecto

```bash
cd TPI-Organizacion-empresarial
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
python main.py
```

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

* ID de solicitud
* DNI del empleado
* Fecha solicitada
* Cantidad de días
* Estado de la solicitud

---

## 🔄 Máquina de Estados

El chatbot utiliza una máquina de estados para mantener el contexto de cada usuario.

Estados principales:

```text
INICIO
ESPERANDO_DNI
VALIDANDO_USUARIO
MOSTRANDO_SALDO
ESPERANDO_FECHA
ESPERANDO_DIAS
VALIDANDO_SOLICITUD
ESPERANDO_APROBACION
SOLICITUD_APROBADA
SOLICITUD_RECHAZADA
```

---

## 🌳 Flujo del Proceso

1. El usuario inicia conversación.
2. El bot solicita identificación.
3. Consulta saldo disponible.
4. Solicita fecha de inicio.
5. Solicita cantidad de días.
6. Verifica reglas de negocio.
7. Simula aprobación.
8. Registra solicitud.
9. Informa resultado al usuario.

---

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

## 🧪 Casos de Prueba

Se incluyen pruebas para:

* Consulta de saldo.
* Registro de solicitudes.
* Validaciones.
* Manejo de errores.

Ubicación:

```text
tests/
```

---

## 🤖 Uso de Inteligencia Artificial

Para el desarrollo del proyecto se utilizaron herramientas de IA como apoyo para:

* Diseño de BPMN.
* Generación de documentación.
* Diseño de casos de prueba.
* Asistencia en programación Python.

Las evidencias se encuentran en:

```text
docs/capturas_IA/
```

---

## 📚 Documentación

### Manual de Usuario

```text
docs/manual_usuario.pdf
```

### Diccionario de Datos

```text
docs/diccionario_datos.pdf
```

---

## 📸 Evidencias

Capturas del funcionamiento del sistema:

```text
screenshots/
```

---

## 📄 Licencia

Proyecto desarrollado exclusivamente con fines académicos para la materia Organización Empresarial.

---

## 🎓 Universidad

**Tecnicatura Universitaria en Programación**

**Organización Empresarial**

**Trabajo Práctico Integrador**
