from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import telegram_bot as t_bot


app = ApplicationBuilder().token("5761018944:AAEAWhwV_0DqO0BLX25ZVc_KNvl7XC5somg").build()

app.add_handler(CommandHandler("Hi", t_bot.hi_user))
print('server START')
app.run_polling()