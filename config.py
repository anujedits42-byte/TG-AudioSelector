import os

# Telegram API credentials - read from environment variables
API_ID = int(os.environ.get("API_ID", "34446649"))
API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8741784728:AAFLpwz7UZvEUumoxgO2I7ii8Lo-9ZSpa1o")

# MongoDB URL
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")

# DB Channel ID
DB_CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", "-1003515041061"))

# Owner user ID
OWNER_ID = 7892805795, 7168219724, 8256962358  # Owner's user ID

# ALLOWED GROUP IDS
ALLOWED_GROUP_IDS = {
    -1003791508617
}

# Maximum file size (e.g., 4GB)
MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB in bytes

# Premium users and daily limits
PREMIUM_USERS = {7892805795, 7168219724, 8256962358}  # Add premium user IDs here
DAILY_LIMIT_FREE = 30  # Videos per day for free users
DAILY_LIMIT_PREMIUM = 60  # Videos per day for premium users

# Download directory
DOWNLOAD_DIR = "./downloads"

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if not os.access(DOWNLOAD_DIR, os.W_OK):
    raise PermissionError(f"No write permission for {DOWNLOAD_DIR}")
