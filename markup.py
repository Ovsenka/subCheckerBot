from aiogram import types
from config import url1, url2, url3, url4, name1, name2, name3, name4



btnWannaAccces = types.KeyboardButton("Хочу получить доступ")

kb_remove = types.ReplyKeyboardRemove()

kb_start = types.ReplyKeyboardMarkup(resize_keyboard=True) 
kb_start.add(btnWannaAccces)

kb_checksub = types.InlineKeyboardMarkup(row_width=1)

btn_check = types.InlineKeyboardButton("Я подписался", callback_data="checksubs")

if url1 != "":
    ch1 = types.InlineKeyboardButton(name1, url=url1)
    kb_checksub.add(ch1)
if url2 != "":
    ch2 = types.InlineKeyboardButton(name2, url=url2)
    kb_checksub.add(ch2)

if url3 != "":
    ch3 = types.InlineKeyboardButton(name3, url=url3)
    kb_checksub.add(ch3)

if url4 != "":
    ch4 = types.InlineKeyboardButton(name4, url=url4)
    kb_checksub.add(ch4)

kb_checksub.add(btn_check)

