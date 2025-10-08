import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💡 Оставить предложение")],
        [KeyboardButton(text="⚠️ Сообщить о проблеме")],
        [KeyboardButton(text="🙏 Поблагодарить коллегу")]
    ],
    resize_keyboard=True
)

feedback_type = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Это бот для анонимной обратной связи.\nВыберите тип сообщения:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text in ["💡 Оставить предложение", "⚠️ Сообщить о проблеме", "🙏 Поблагодарить коллегу"])
async def handle_feedback_type(message: types.Message):
    feedback_type[message.from_user.id] = message.text
    await message.answer("Пожалуйста, напишите ваш текст сообщения:")

@dp.message(lambda message: message.from_user.id in feedback_type)
async def save_feedback(message: types.Message):
    now = datetime.now().strftime("%d.%m.%Y, %H:%M")
    type_map = {
        "💡 Оставить предложение": "💡 Новое предложение",
        "⚠️ Сообщить о проблеме": "⚠️ Сообщение о проблеме",
        "🙏 Поблагодарить коллегу": "🙏 Благодарность"
    }
    feedback = type_map.get(feedback_type[message.from_user.id], "")
    formatted_message = f"{feedback}\n_{message.text}_\n🕓 {now}"
    await bot.send_message(ADMIN_ID, formatted_message)
    await message.answer("✅ Спасибо за обратную связь!\nСообщение передано руководителю.")
    feedback_type.pop(message.from_user.id)

async def main():
    print("✅ Бот запущен... Ждём сообщений")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())