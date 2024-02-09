from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from telebot.types import Update
import telebot
import requests
from telebot import types



TOKEN = '6957575391:AAHjHq2lFnoCjikPk8ogNiSq_BeebeLMmKk'

BACKEND_URL = 'http://35.232.206.28'

bot = telebot.TeleBot(TOKEN)

@method_decorator(csrf_exempt, name='dispatch')
class TelegramBotView(View):
    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = Update.de_json(json_str)
        self.bot.process_new_updates([update])
        return JsonResponse({'status': 'ok'})

    def image_send(self,image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            with open('product_image.jpg', 'wb') as file:
                file.write(response.content)

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Продукты'))
    keyboard.add(telebot.types.KeyboardButton('Продукты по категориям'))
    keyboard.add(telebot.types.KeyboardButton('Команды'))



    @bot.message_handler(commands=['start'])
    def handle_start(self,message):
        bot.send_message(message.chat.id, 'Привет! Этот бот поможет вам найти данные на сайте EcoUse. Используйте кнопки ниже. ', reply_markup=keyboard)

    @bot.message_handler(commands=['help'])
    def handle_help(self,message):
        commands_list = "\n".join([
            "/start - Начать общение с ботом",
            "/help - Получить список команд",
            "/products - Найти данные о продуктах",
            "/category - Получить данные по категориям"
        ])
        bot.send_message(message.chat.id, f"Доступные команды:\n{commands_list}")


    @bot.message_handler(commands=['products'])
    def handle_search(self,message):
        search_url = f'{BACKEND_URL}/products/'

        response = requests.get(search_url)

        result_data = response.json().get('results')

        if result_data:
            for product in result_data:
                title = product.get('title', 'Нет заголовка')
                body = product.get('body', 'Нет описания')
                image = product.get('image', None)
                price = product.get('price', 'Нет цены')
                created_at = product.get('created_at', 'Нет даты создания')

                message_text = f"Назание: {title}\n\n Описание: {body}\nЦена: {price}\nДата создания: {created_at}"

                # bot.send_message(message.chat.id, message_text)
                self.image_send(image)
                image = 'product_image.jpg'
                with open(image, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo=photo, caption=message_text)
            
        else:
            bot.send_message(message.chat.id, 'Нет результатов по вашему запросу')



    @bot.message_handler(commands=['category'])
    def handle_category(self,message):
        keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        response = requests.get(f'{BACKEND_URL}/category/')

        if response.status_code == 200:
            response_data = response.json()
            categories = [category['name'] for category in response_data]

            for category in categories:
                keyboard_category.add(types.KeyboardButton(category))

            bot.send_message(message.chat.id, 'Выберите категорию:' , reply_markup=keyboard_category)


            # @bot.message_handler(func=lambda message: True)
            # def handle_button(message):
            #     if message.text == 'window':
            #         bot.send_message(message.chat.id, 'Вы нажали на кнопку')

            #     elif message.text == 'doors':
            #         bot.send_message(message.chat.id, 'Вы нажали на кнопку 2')

                
        else:
            bot.send_message(message.chat.id, f'Ошибка при запросе к бекенду: {response.status_code}')



    @bot.message_handler(func=lambda message: True)
    def handle_buttons(self,message):
        if message.text == 'Продукты':
            self.handle_search(message)
        elif message.text == 'Продукты по категориям':
            self.handle_category(message)
        elif message.text == 'Команды':
            self.handle_help(message)
        elif message.text == 'doors':
            bot.send_message(message.chat.id, 'Вы нажали на кнопку 2')



telegram_bot_view = TelegramBotView.as_view()
