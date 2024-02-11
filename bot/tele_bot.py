import telebot
import requests
from telebot import types



TOKEN = '6957575391:AAHjHq2lFnoCjikPk8ogNiSq_BeebeLMmKk'

BACKEND_URL = 'http://localhost'

bot = telebot.TeleBot(TOKEN)

def image_send(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('product_image.jpg', 'wb') as file:
            file.write(response.content)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton('Продукты'))
keyboard.add(telebot.types.KeyboardButton('Продукты по категориям'))
keyboard.add(telebot.types.KeyboardButton('Команды'))

response = requests.get(f'{BACKEND_URL}/category/')

if response.status_code == 200:
    response_data = response.json()
    categories = {category['name']:category['id'] for category in response_data}
    


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот поможет вам найти данные на сайте EcoUse. Используйте кнопки ниже. ', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    commands_list = "\n".join([
        "/start - Начать общение с ботом",
        "/help - Получить список команд",
        "/products - Найти данные о продуктах",
        "/category - Получить данные по категориям"
    ])
    bot.send_message(message.chat.id, f"Доступные команды:\n{commands_list}")


@bot.message_handler(commands=['products'])
def handle_search(message):
    search_url = f'{BACKEND_URL}/products/products/'

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
            image_send(image)
            image = 'product_image.jpg'
            with open(image, 'rb') as photo:
                bot.send_photo(message.chat.id, photo=photo, caption=message_text)
         
    else:
        bot.send_message(message.chat.id, 'Нет результатов по вашему запросу')



@bot.message_handler(commands=['category'])
def handle_category(message):
    keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    response = requests.get(f'{BACKEND_URL}/category/')

    if response.status_code == 200:
        response_data = response.json()
        categories = [category['name'] for category in response_data]

        for category in categories:
            keyboard_category.add(types.KeyboardButton(category))

        bot.send_message(message.chat.id, 'Выберите категорию:' , reply_markup=keyboard_category)
            
    else:
        bot.send_message(message.chat.id, f'Ошибка при запросе к бекенду: {response.status_code}')



@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Продукты':
        handle_search(message)
    elif message.text == 'Продукты по категориям':
        handle_category(message)
    elif message.text == 'Команды':
        handle_help(message)
    elif message.text in categories.keys():
        category_name = categories[message.text]
        response = requests.get(f'{BACKEND_URL}/products/category/{category_name}/',)
        result_data = response.json()

        if result_data:
            for product in result_data :
                title = product.get('title', 'Нет заголовка')
                body = product.get('body', 'Нет описания')
                image = product.get('image', None)
                price = product.get('price', 'Нет цены')
                created_at = product.get('created_at', 'Нет даты создания')

                

                message_text = f"Назание: {title}\n\n Описание: {body}\nЦена: {price}\nДата создания: {created_at}"
                image_send(image)
                print(image_send)
                image = 'product_image.jpg'
                with open(image, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo=photo, caption=message_text)
            
        else:
            bot.send_message(message.chat.id, 'Нет результатов по вашему запросу')



if __name__ == '__main__':
    bot.polling(none_stop=True)



