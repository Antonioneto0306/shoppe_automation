import os
from dotenv import load_dotenv

load_dotenv()  # lê o .env

PARTNER_ID = os.getenv("PARTNER_ID")
PARTNER_KEY = os.getenv("PARTNER_KEY")
SHOP_ID = os.getenv("SHOP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REDIRECT_URL = os.getenv("REDIRECT_URL")
