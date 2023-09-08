import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InputMediaAudio, InputMediaPhoto, FSInputFile
from aiogram.utils.markdown import hbold
from codes import codes

TOKEN = "6404433706:AAER8qmZIPY4nfjqM-BTKiVNo3-CG5YoMso"

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Вводи свой первый код!")


@dp.message()
async def answer(message: types.Message) -> None:
    text = message.text
    if text and codes.get(text):
        files = codes.get(text)

        if files.get("audio"):
            audios = [files.get('audio')] if not isinstance(files.get('audio'), list) else files.get('audio')
            audios_list = [InputMediaAudio(type="audio",
                                           media=FSInputFile(f"files/audios/{audio}")) for audio in audios]
            await bot.send_media_group(message.chat.id, media=audios_list)

        if files.get("photo"):
            photos = [files.get('photo')] if not isinstance(files.get('photo'), list) else files.get('photo')
            photos_list = [
                InputMediaPhoto(type="photo",
                                media=FSInputFile(f"files/photos/{photo}")) for photo in photos
            ]
            await bot.send_media_group(message.chat.id, media=photos_list)

        if files.get("text"):
            with open(f"files/texts/{files.get('text')}", "r", encoding="utf-8") as file:
                text = file.read()
            await bot.send_message(message.chat.id, text)

    else:
        await message.answer("Что-то не так, попробуй ещё раз!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bye!")
