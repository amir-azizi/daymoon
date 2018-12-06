#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:12:10 2018

@author: amir
"""

import telebot
#import config
import dm_function
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import timezone

bot_token = #ask me for it
bot = telebot.TeleBot(bot_token)
#TODO: get the id from new starts
chat_id = -355590034 #for the 'Daymmon-group' in Bochum

#TODO: get times from the host device
cest = timezone('Europe/Berlin')
sched = BlockingScheduler()
sched.configure(timezone=cest)
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
def scheduled_job():
    out_message = dm_function.daymoon()
    if out_message != '--':
        bot.send_message(chat_id, out_message)

sched.start()
