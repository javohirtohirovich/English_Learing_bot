import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordDefination import get_defination
from googletrans import Translator

translator=Translator()
API_TOKEN = '6049855735:AAHc2nchoYoW1rnswajQS8jywGOLiy8-JrE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu alaykum!\nMen Ingiliz tili bo'yicha\nYordamchi Botman.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Botdan foydalanish:\n1) Agarda siz 1 ta yoki 2 ta so'z yuborsangiz\n"
                        "Men sizga Ingiliz tilida to'liq tushuntirib beraman\n"
                        "va talafuz qilishengiz uchun audio yuboraman\n"
                        "2) Agarda siz 2 tadan ortiq so'z yuborsangiz\n"
                        "Men sizga uni O'zbek tiliga tarjima qilib qaytaraman")


@dp.message_handler()
async def trans(message: types.Message):
    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        til='uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text,til).text)
    else:
        if lang=='en':
            word=message.text
        else:
            word=translator.translate(message.text,dest='en').text
        lookup=get_defination(word)
        if lookup:
            await message.reply(f"Word: {word} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audioFile'):
                await message.reply_voice(lookup['audioFile'])
        else:
            await message.reply("🤔Bunday so'z topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)