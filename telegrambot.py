from telegram.ext import *

API_KEY = "7018654978:AAH6S7ZSMGHVKZg35_aCRM3sF-gOWDJzN1I"

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dipatcher

    dp.app_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(1.0)
    updater.idle()

