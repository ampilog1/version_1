from django.core.management.base import BaseCommand
from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
from learning_app.models import *
import asyncio


bot = AsyncTeleBot(settings.TELEGRAM_BOT_API_KEY)


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
async def first_vacancy_20(message):
    chat_id = message.chat.id
    vacancy_all = Vacancy.objects.values()
    for vacancy_prep in vacancy_all[:20]:
        vacancy_send = str([value for value in vacancy_prep.values() if value is not None])
        # vacancy_send = [value for value in vacancy_prep.values() if value is not None]
        # for value in vacancy_prep_vision:
        #     if value is not None:
        # vacancy_send = [f'{value}' for value in vacancy_prep.values()]
        await bot.send_message(chat_id, vacancy_send)


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
