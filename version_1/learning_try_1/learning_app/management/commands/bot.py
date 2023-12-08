from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from learning_app.models import *


bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@bot.message_handler(commands=['huy'])
def parse_site(message):
    text = message.text.split()[1]
    chat_id = message.chat.id
    vacancy_all = Vacancy.objects.values()
    for vacancy_send in vacancy_all[:20]:
        for key, value in vacancy_send
            bot.send_message(chat_id, f'{key} - {vacancy_send[key]}')


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **options):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
