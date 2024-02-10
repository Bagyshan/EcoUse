FROM python:3.11-slim

ENV PYTHONIOENCODING UTF-8

# Создаем каталог для статических файлов
RUN mkdir -p /usr/src/app/static

WORKDIR /usr/src/app/

COPY static/ /usr/src/app/static/
RUN ls -R /usr/src/app/static/


# Копируем файлы проекта
COPY . .

# Установка зависимостей
RUN apt-get update \
    && apt-get install -y libpq-dev

# Устанавливаем зависимости Python
COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
