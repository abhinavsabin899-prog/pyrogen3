import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Group Manager Bot is online!\nUse /help to see commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/id - Get your ID\n"
        "/ban - Ban a replied user\n"
        "/kick - Kick a replied user"
    )

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Your ID: {update.effective_user.id}\n"
        f"Chat ID: {update.effective_chat.id}"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing in Environment Variables")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", id_command))
    app.run_polling()

if __name__ == "__main__":
    main()
