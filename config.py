from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "24509589"))
API_HASH = getenv("API_HASH", "717cf21d94c4934bcbe1eaa1ad86ae75")

BOT_TOKEN = getenv("BOT_TOKEN", "6982870876:AAG7aKl5xkjjEnWMRpA39wZKH8OKexS8RHY")
OWNER_ID = int(getenv("OWNER_ID", "7070591202"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Somu:Somu@somu.xbkiklu.mongodb.net/?retryWrites=true&w=majority&appName=Somu")
MUST_JOIN = getenv("MUST_JOIN", "somueditingzone")
DAXX_API = getenv("DAXX_API", "daxx-1490?api+key:free")
