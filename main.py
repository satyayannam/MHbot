from typing import Final
from telegram import InputFile
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from datetime import datetime


TOKEN: Final = '6501972147:AAGdF8_MHQInW4GV7UioeTPb6ot2IcDtaAs'

BOT_USERNAME: Final= '@MoneyHiker_bot'

async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_path = r'C:\Users\Satya Yannam\Desktop\MHBOT\qrr.jpg'
    await update.message.reply_text("Please paste the transaction id to process your payment following by txid ex:'txid: xxxxxxxxxxxx'")
    await update.message.reply_text('8555895984460@paytm')

    try:
        with open(image_path, 'rb') as photo:
            await update.message.reply_photo(photo=photo)
    except FileNotFoundError:
        await update.message.reply_text("Image not found.")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello investors! thanks for choosing me. I am a bot that has the ability to choose various money markets to invest you your money wisely and provide you with a guaranteed profits within a hour or two")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello investors! I am here to help you, in a nutshell this bot is an AI investors with ability that invests your money in various money markets and provide you with guaranteed returns and no losses")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello investors! thanks for choosing me. I am a bot that has the ability to choose various money markets to invest you your money wisely and provide you with a guaranteed profits within a hour or two")


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if any(greeting in processed for greeting in ['hi', 'hello', 'hey']):
        return 'Hey investor!'
    if 'txid' in processed: 
        return "ok we will ensure your transaction, please ensure you pasted correct transaction id"
    else:
        return('Iam just a bot, please using the following commands for more options /start, /investcode, /about')
    
    return None






async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text.lower() 

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if any(greeting in text for greeting in ['hi', 'hello', 'hey']):
        reply_text = "Hello investor! If you want to start investing, click here /investcode"
        await update.message.reply_text(reply_text)
    elif 'admin' in text:
        reply_text = "Please text the issue you want to let the admin know."
        await update.message.reply_text(reply_text)

    print(f'{current_time} - User({update.message.chat.id}) : {text}')

    response = handle_response(text)
    await update.message.reply_text(response)












async def error(update: Update, context:  ContextTypes,Default_Type):
    print(f'Update {update} caused error {context.error} ')

if __name__ == '__main__':
    print('activating...')
    app= Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('investcode', image_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    

    app.add_error_handler(error)
    print('running...')
    app.run_polling(poll_interval=3)


