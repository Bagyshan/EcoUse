FROM python:3.8

# Установите зависимости
RUN pip install python-telegram-bot

# Копируйте код бота в образ
COPY . /app

# Установите рабочую директорию
WORKDIR /app

# Запустите бот
CMD ["python", "tele_bot.py"]