import time
from pyrogram import Client, filters
from pyrogram.types import Message
from proxybot import COMMAND_HAND_LER
from proxybot.utils.custom_filters import dev_filter


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & dev_filter)
async def ping(c: Client, m: Message):
    start = time.time()
    reply = await m.reply_text("Pinging...", reply_to_message_id=m.message_id)
    delta_ping = time.time() - start
    await reply.edit_text(
        f"**Pong!**\n`{delta_ping * 1000:.3f} ms`",
        parse_mode="markdown",
    )
    return
