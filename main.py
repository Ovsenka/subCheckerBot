import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import message

from config import TOKEN_API, url1, url2, url3, url4
from markup import kb_checksub, kb_remove, kb_start

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

if "t.me/" in url1:
    id_1 = "@" + url1.split("t.me/")[1]
if "t.me/" in url2:
    id_2 = "@" + url2.split("t.me/")[1]
if "t.me/" in url3:
    id_3 = "@" + url3.split("t.me/")[1]
if "t.me/" in url4:
    id_4 = "@" + url4.split("t.me/")[1]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! В этом чат-боте ты получишь доступ к уникальному контенту!", reply_markup=kb_remove)
    await asyncio.sleep(2)
    await message.answer("Жми на кнопку ниже👇", reply_markup=kb_start)

@dp.message_handler()
async def get_access(message: types.Message):
    if message.text == "Хочу получить доступ":
        await message.reply("Подпишитесь на каналы", reply_markup=kb_checksub)

@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    if call.data == "checksubs":
        if "t.me/" in url1:    
            s_ch1 = await bot.get_chat_member(chat_id=id_1, user_id=call.message.chat.id)
        else:
            s_ch1 = {"status":"notstated"}
        
        if "t.me/" in url2:
            s_ch2 = await bot.get_chat_member(chat_id=id_2, user_id=call.message.chat.id)
        else:
            s_ch2 = {"status":"notstated"}

        if "t.me/" in url3:
            s_ch3 = await bot.get_chat_member(chat_id=id_3, user_id=call.message.chat.id)
        else: 
            s_ch3 = {"status":"notstated"}
        
        if "t.me/" in url4:
            s_ch4 = await bot.get_chat_member(chat_id=id_4, user_id=call.message.chat.id)
            if s_ch1["status"] != 'left' and s_ch2["status"] != 'left' and s_ch3["status"] != 'left' and s_ch4["status"] != 'left':
                await bot.send_message(call.from_user.id, "Отлично! Вот ссылка на доступ к чату!🙂 \n (Ссылка)", reply_markup=kb_remove)
                await bot.delete_message(call.from_user.id, call.message.message_id)
                await asyncio.sleep(5)
                await bot.send_message(call.from_user.id, "Сообщение")
            else:
                await bot.delete_message(call.from_user.id, call.message.message_id)
                await bot.send_message(call.from_user.id, 'Вы не подписались на все каналы! Подпишитесь и нажмите кнопку заново', reply_markup=kb_checksub)   
        else:
            if s_ch1["status"] != 'left' and s_ch2["status"] != 'left' and s_ch3["status"] != 'left':
                await bot.send_message(call.from_user.id, "Отлично! Вот ссылка на доступ к чату!🙂 \n (Ссылка)", reply_markup=kb_remove)
                await bot.delete_message(call.from_user.id, call.message.message_id)
                await asyncio.sleep(5)
                await bot.send_message(call.from_user.id, "Сообщение")


            else:
                await bot.delete_message(call.from_user.id, call.message.message_id)
                await bot.send_message(call.from_user.id, 'Вы не подписались на все каналы! Подпишитесь и нажмите кнопку заново', reply_markup=kb_checksub)
                

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



