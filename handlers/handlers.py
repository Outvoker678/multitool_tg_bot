from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F

from keyboards.keyboard import start_keyboard, start_inl_keyboard

router = Router()


@router.message(F.text == "Мой ID")
async def my_id_handlers(message: Message) -> None:
    """Обработчик "Мой ID"."""
    await message.answer(
        f"<b>Ваш Telegram ID</b>:\n{message.from_user.id}",
        parse_mode="HTML")


@router.message(F.text == "Мои друзья")
async def my_friends_handlers(message: Message) -> None:
    """Обработчик "Мой ID"."""
    await message.answer(
        f"<b>В разработке</b>",
        parse_mode="HTML")
    
    
@router.message(F.text == "Заявки")
async def requests_handlers(message: Message) -> None:
    """Обработчик "Мой ID"."""
    await message.answer(
        f"<b>В разработке</b>",
        parse_mode="HTML")


@router.message(F.text == "Добавить друга")
async def add_driends_handlers(message: Message) -> None:
    """Обработчик "Мой ID"."""
    await message.answer(
        f"<b>В разработке</b>",
        parse_mode="HTML")


@router.callback_query(F.data == "help_add_friends")
async def add_driends_handlers(callback: CallbackQuery) -> None:
    """Обработчик "Мой ID"."""
    await callback.answer("")
    await callback.message.edit_text(
        "Чтобы отправлять видео друзьям, сначала добавьте их по инструкции ниже:\n"
        "1. Нажмите <b>Мой ID</b> и отправьте свой ID другу.\n"
        "2. Друг должен ввести ваш ID через меню <b>Добавить друга</b>.\n"
        "3. После этого вы увидите заявку в меню <b>Заявки</b> и сможете её принять.\n\n"
        "Или наоборот: пусть друг отправит вам свой ID, а вы добавьте его через <b>Добавить друга</b> и примите заявку в <b>Заявки</b>.\n\n"
        "После добавления друзей вы сможете отправлять им скачанные видео — просто нажмите на кнопку под нужным видео!",
        parse_mode="HTML")


@router.message(CommandStart)
async def start_handlers(message: Message) -> None:
    """Обработчик команды /start."""
    await message.answer(
        "<b>👋 Привет! Я бот Multi Tool.</b>\n\n"
        "Я могу:\n"
        "<b>• Скачивать видео из TikTok</b>\n"
        "<b>• Скачивать музыку из Spotify</b>\n\n"
        "<i>Для этого просто отправьте мне ссылку — и я всё загружу!</i>\n\n",
        parse_mode="HTML", reply_markup=start_keyboard)
    await message.answer("Также я могу отправлять их вашим друзьям.\n",
                         reply_markup=start_inl_keyboard)
