import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


BOT_TOKEN="8565436292:AAHDnqEZcB1y8V_byxq3i5otteXQyuDxBeA"

bot = Bot(token=BOT_TOKEN)
dp =Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("h1! I am test bot. WORKS OK! Welcome")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
