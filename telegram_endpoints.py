#from dotenv import load_dotenv
from telegram import Update
#import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#load_dotenv()
#telegramtoken = os.getenv("TELEGRAMTOKEN")
telegramtoken = "6732986203:AAHGwlfWWgxTR06libiEOZyMDB1nrCiYwjU"
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = context.args[0] if context.args else "Hello"
    await update.message.reply_text(f'{text} {update.effective_user.first_name}')

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

app = ApplicationBuilder().token(telegramtoken).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("hi", hi))

app.run_polling()
