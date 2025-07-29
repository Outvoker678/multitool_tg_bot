from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_inl_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Как отправить друзьям?", callback_data="help_add_friends")]])

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Мой ID"), KeyboardButton(text="Мои друзья")],
    [KeyboardButton(text="Заявки"), KeyboardButton(text="Добавить друга")]
], resize_keyboard=True)
