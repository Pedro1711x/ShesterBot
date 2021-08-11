from logging import shutdown
import os
import sys

from telegram.ext import Updater, CommandHandler, updater
def start(update, context):
    update.message.reply_text('Bienvenido! Soy Shester tu asistente personal')
    update.message.reply_text('En que te puedo ayudar?')
def shutdown(update, context):
    update.message.reply_text('Muy bien! ya apagaré el servidor')
    os.system('ssh root@172.20.0.227 ./apagado.sh')
    update.message.reply_text('Listo! está en proceso de apagado.')
if __name__ == '__main__':
    updater = Updater(token='1763183270:AAFVXNn_ChY4FaLvKRteTb2axqjKSe8fwMs', use_context=True)
    dp =updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('shutdown', shutdown))
    
    updater.start_polling()
    updater.idle