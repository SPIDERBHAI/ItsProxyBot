import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

if bool(os.environ.get("ENV", False)):
    from proxybot.sample_config import Config
else:
    from proxybot.config import Development as Config


LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
TMP_DIR = Config.TMP_DIR
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
CONTACT_OWNER = Config.CONTACT_OWNER
DEV_USERS = Config.DEV_USERS
AUTH_GROUP = Config.AUTH_GROUP
AUTH_GROUP_USERNAME = Config.AUTH_GROUP_USERNAME
BOT_VERSION = Config.BOT_VERSION
OWNER_ID = Config.OWNER_ID
MESSAGE_DUMP = Config.MESSAGE_DUMP

if not os.path.isdir(TMP_DIR):
    os.makedirs(TMP_DIR)
