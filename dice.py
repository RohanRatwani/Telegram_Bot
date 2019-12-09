import time
import random
import datetime
import telepot
import os
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if command == 'time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == 'hi':
        bot.sendMessage (chat_id, str("Hi! This is Atila How Can I help you today?"))
    elif command == 'time':
        bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == 'logo':
        bot.sendPhoto (chat_id, photo = "https://images.app.goo.gl/TWFXwEw9D7GMMeGU7")
    elif command == 'myStevens':
        bot.sendMessage (chat_id, str("https://shibboleth.stevens.edu"))
    elif command == 'curriculum':
        bot.sendMessage (chat_id, str("https://www.stevens.edu/sites/stevens_edu/files/files/academic-catalog/Stevens-2018-2019-Academic-Catalog.pdf"))
    elif command == 'IoT_Projects':
        bot.sendMessage (chat_id, str("https://github.com/kevinwlu/iot/tree/master/projects"))
bot = telepot.Bot('1033013602:AAFwyWhCVdbg1dKL-HC_Oy4aYZtup_8IUWg')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
