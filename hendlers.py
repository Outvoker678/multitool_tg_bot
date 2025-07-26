from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message()
async def cmd_start(message: Message):
    await message.answer("Привет!")