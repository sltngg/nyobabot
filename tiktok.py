# Copyright (C) 2020-2021 by BukanDev@Github, < https://github.com/BukanDev >.
#
# This file is part of < https://github.com/BukanDev/TikTokDL > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/BukanDev/TikTokDL/blob/main/LICENSE >
# @pySmartDL
#
# All rights reserved.


import os
import telebot
from telebot import types
import requests

TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN)
me = bot.get_me()
print(f'Bot telah aktif @{me.username}')


@bot.message_handler(commands=['start', 'help'])
def start_message(m):
	bot.send_message(m.chat.id, '*Bot Sibuk Bos*', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def tiktokdl(m):
    if m.text.startswith(('https://www.tiktok.com', 'http://www.tiktok.com', 'https://vm.tiktok.com', 'https://vt.tiktok.com')):
        try:
            send = bot.reply_to(m, 'Sik Loading...')
            url = requests.get(f'https://api.douyin.wtf/api?url={m.text}').json()
            video = url.get('nwm_video_url', None)
#            audio = url.get('video_music_url', None)
#            videotitle = url['video_title']
#            videomusictitle = url['video_music_title']
#            autor = url['video_author_nickname']
#            time = url['analyze_time']
            bot.send_video(m.chat.id, video, caption=f'{m.text}', reply_to_message_id=m.message_id, parse_mode='Markdown')
#            bot.send_audio(m.chat.id, audio, reply_to_message_id=m.message_id)
            bot.delete_message(m.chat.id, send.message_id)
            
        except Exception as e:
            print(e)
            bot.edit_message_text(f'_Link e kleru_', m.chat.id, message_id=send.message_id, parse_mode='Markdown')
        
bot.infinity_polling()
