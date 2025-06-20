import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --------------------------------- #

API_ID = 20948356
API_HASH = "6b202043d2b3c4db3f4ebefb06f2df12"
BOT_TOKEN = "7703532604:AAEZO0Nk98N7EJcncvPzeoX1EqGi4L0_b5k"
MONGO_DB_URI = "mongodb+srv://Combobot:Combobot@combobot.4jbtg.mongodb.net/?retryWrites=true&w=majority&appName=Combobot"

# --------------------------------- #

STATS_VIDEO = "https://unitedcamps.in/Images/file_5250.jpg"
START_VIDEO = "https://i.ibb.co/nsyp67FS/Img2url-bot.jpg"
HELP_MENU_VIDEO = "https://i.ibb.co/Z64Z3yCR/Img2url-bot.jpg"
HELP_VIDEO_1 = "https://i.ibb.co/8gkx23jt/Img2url-bot.jpg"
HELP_VIDEO_2 = "https://i.ibb.co/S7Z4fHJt/Img2url-bot.jpg"
HELP_VIDEO_3 = "https://unitedcamps.in/Images/file_11453.jpg"
HELP_VIDEO_4 = "https://unitedcamps.in/Images/file_11454.jpg"

# --------------------------------- #

LOGGER_ID = -1002059639505
OWNER_ID = 7394132959

# --------------------------------- #

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# --------------------------------- #

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PacificArc")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/phoenixXsupport")

# --------------------------------- #

if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")