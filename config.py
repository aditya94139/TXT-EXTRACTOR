import os
from os import getenv

API_ID = int(os.environ.get("25586552", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("f265cba9d76dc6ad70914accbe758f47", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("1368753935", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("7062964338", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://jangidudit45:Gautam5257@cluster0.s8fbcy9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("-1002309403385", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
