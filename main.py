import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command




load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = Bot(token=token)
dp =Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("h1! I am test bot. WORKS OK! Welcome")

@dp.message(Command("test"))
async def test_command(message: Message):
    await message.answer("NEW test fuction is works!) CONGARTS!)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
