# Установка Docker и Docker-compose

Для того чтобы запустить проект вам нужно установить Docker и Docker-compose.

## Обновите систему командой:

```
sudo apt update && sudo apt upgrade
```

## Установите Docker

```
sudo apt install -y docker.io
```

## Зарегистрируйте своего пользователя, чтобы запускать команды без sudo:

```
sudo usermod -aG docker $USER
```

## Установите Docker-compose:

```
sudo apt install -y docker-compose
```

## Заполните файл .env по примеру env_example


## Запустите команду: 

```
docker-compose up --build
```



### Для создания админа:

```
docker-compose start
docker-compose exec web bash
./manage.py createsuperuser
```

### Для запуска телеграмм бота использвуйте команду:

```
docker-compose start
docker-compose exec web bash
python telebot
```
