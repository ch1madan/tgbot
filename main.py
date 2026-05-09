import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from db import init_db, log_user

load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher()

# init DB при старте
init_db()


@dp.message(Command("start"))
async def start_command(message: Message):
    log_user(message.from_user, "/start")
    await message.answer("h1! I am test bot. WORKS OK! Welcome")


@dp.message(Command("test"))
async def test_command(message: Message):
    log_user(message.from_user, "/test")
    await message.answer("NEW test function works! CONGRATS!")


# логируем ВСЕ остальные сообщения
@dp.message()
async def catch_all(message: Message):
    log_user(message.from_user, message.text)
    await message.answer("logged")
    

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
