from pyrogram import Client
from pyrogram import __version__
from pyrogram.raw.all import layer

from proxybot import APP_ID, API_HASH, LOGGER, BOT_TOKEN, TMP_DIR, MESSAGE_DUMP


class ProxyBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DIR,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=16,
        )

    async def start(self):
        await super().start()

        me = await self.get_me()
        LOGGER.info(
            f"ItsProxyBot based on Pyrogram v{__version__}\n"
            f"(Layer {layer}) started on @{me.username}"
        )
        # Send message to MESSAGE_DUMP Log Channel
        await self.send_message(MESSAGE_DUMP, "<b><i>Bot Started!</i></b>")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("ItsProxyBot stopped...!\nkthxbye!")


if __name__ == "__main__":
    ProxyBot().run()
