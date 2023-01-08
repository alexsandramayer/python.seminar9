from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logger as log


async def hi_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.logger(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


