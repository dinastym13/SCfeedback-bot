# Telegram Feedback Bot

## Как запустить локально
1. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте `.env` файл:
```
TOKEN=ваш_токен_бота
ADMIN_ID=ваш_admin_id
```

4. Запустите бота:
```bash
python bot.py
```

## Как запустить на Render.com
1. Загрузите этот проект в GitHub.
2. На Render создайте новый Web Service.
3. В поле Start Command напишите:
```
python bot.py
```
4. В Environment Variables добавьте:
```
TOKEN=ваш_токен_бота
ADMIN_ID=ваш_admin_id
```

Render сам установит зависимости из requirements.txt и запустит бота.# SCfeedback
# SCfeedback
