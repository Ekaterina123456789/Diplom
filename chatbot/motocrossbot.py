import asyncio
import logging
import sys

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

BOT_TOKEN = '6352758599:AAFo7JXyfmXxfk_6MtOtyLSMGGH57eMzphE'
OMDB_API_KEY = '94893d00'

dp = Dispatcher()


@dp.message()
async def search_movie(message: types.Message):
    words = message.text.split()
    if words[0] != 'film' and words[0] != '/film':
        await message.reply('Command not found!')
        return
    year = None
    title = None
    if len(words) >= 3:
        words.pop(0)
        title = ''
        while not words[0].isdigit():
            title += words[0] + ' '
            words.pop(0)
            if len(words) == 0:
                break
        else:
            year = words[0]
    elif len(words) == 2:
        title = words[1]
    else:
        await message.reply('Specify a film name!')
        return

    omdb_url = f'https://www.omdbapi.com/?apikey={OMDB_API_KEY}'
    omdb_url += f'&t={title}'

    response = requests.get(omdb_url)
    movie_data = response.json()
    if movie_data['Response'] == 'True':
        message_text = f'<b>Title:</b> {movie_data["Title"]}\n' \
                        f'<b>Genre:</b> {movie_data["Genre"]}\n' \
                        f'<b>Release Date:</b> {movie_data["Released"]}\n' \
                        f'<b>Rated:</b> {movie_data["Rated"]}\n' \
                       f'<b>Duration:</b> {movie_data["Runtime"]}\n' \
                       f'<b>Rated:</b> {movie_data["Rated"]}\n' \
                       f'<b>Actors:</b> {movie_data["Actors"]}\n' \
                       f'<b>Languages:</b> {movie_data["Language"]}\n' \

        ratings = movie_data['Ratings']
        for rating in ratings:
            message_text += f'<b>{rating["Source"]}: </b> {rating["Value"]}\n'

        message_text += f'<a href="{movie_data["Poster"]}">Source</a>'
        await message.reply(message_text)
    else:
        await message.reply('Film was not found')


async def main():
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    asyncio.run(main())
