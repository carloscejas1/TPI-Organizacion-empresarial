from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import TOKEN

from handlers import (
    start,
    mensajes,
    consultar,
    aprobar,
    rechazar,
    ayuda
)

def main():

    print("Iniciando aplicación...")

    app = Application.builder().token(TOKEN).build()

    print("Aplicación creada")

    app.add_handler(
        CommandHandler("start", start)
        )
    app.add_handler(
        CommandHandler("consultar", consultar)
        )
    app.add_handler(
        CommandHandler("aprobar", aprobar)
        )
    app.add_handler(
        CommandHandler("rechazar", rechazar)
        )
    app.add_handler(
        CommandHandler("ayuda", ayuda)
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