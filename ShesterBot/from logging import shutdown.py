
from collections import UserList
from functools import wraps
from logging import shutdown
import os
import sys
import time
import numbers
import subprocess
from subprocess import PIPE
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler)

def start(update, context):
    update.message.reply_text('Bienvenido! Soy Shester tu asistente personal')  
    update.message.reply_text('En que te puedo ayudar?')
def shutdown(update, context):
    update.message.reply_text('Muy bien! ya apagaré el servidor')
    os.system('ssh root@172.20.0.227 ./apagado.sh')
    update.message.reply_text('Listo! está en proceso de apagado.')
def contenedor(update, context):
    update.message.reply_text('Muy bien, te mostrare los contenedores.')
    #output= subprocess.call(['ssh', 'root@172.20.0.227', 'pct', 'list'], capture_output=True)
    output=subprocess.run(['ssh', 'root@172.20.0.227', 'pct', 'list'], capture_output=True)
    #print(output.stdout)
    #subprocess('ssh root@172.20.0.227 pct list')
    update.message.reply_text('Estos son tus contenedores')
    update.message.reply_text(str(output.stdout))
if __name__ == '__main__':
    updater = Updater(token='1763183270:AAFVXNn_ChY4FaLvKRteTb2axqjKSe8fwMs', use_context=True)
    ID= 938559800

    dp =updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('shutdown', shutdown))
    dp.add_handler(CommandHandler('contenedor', contenedor))

    updater.start_polling()
    updater.idle