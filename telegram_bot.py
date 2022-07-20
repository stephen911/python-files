from telegram import *
from telegram.ext import *
# pip install python-telegram-bot
bot = Bot("1530686883:AAGKLwV3tNz9JiXS1Wj2KGk_3kMgovPD_Yc")
updater = Updater("1530686883:AAGKLwV3tNz9JiXS1Wj2KGk_3kMgovPD_Yc", use_context=True)
dispatcher = updater.dispatcher


def message(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="http//:stedap1.site.live"
)


start_value = CommandHandler("hello", message)
dispatcher.add_handler(start_value)
updater.start_polling()
