class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", "1309301"))
    API_HASH = os.environ.get("API_HASH", "92ff1ebdc07145c2c1d3d6dc04afccb5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1219959468:AAFyqhZoj6IAdZU9bIyJg8aQT24ntxqDU54")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")
    TMP_DIR = os.environ.get("TMP_DIR", "./TEMP/")
    CONTACT_OWNER = os.environ.get("CONTACT_OWNER", None)
    DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    BOT_VERSION = os.environ.get("BOT_VERSION", "Development")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1110765912")
    MESSAGE_DUMP = int(os.environ.get("MESSAGE_DUMP", -100))


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
