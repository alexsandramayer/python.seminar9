from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def logger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('logger.csv', 'a')
    file.write(f'{update.effective_user.first_name}\n')
    file.close()