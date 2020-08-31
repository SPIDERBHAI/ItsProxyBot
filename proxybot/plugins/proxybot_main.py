import os
import urllib.parse
import proxygrab
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message,
)
from proxybot import COMMAND_HAND_LER


proxytypes = ["HTTP", "HTTPS", "Socks4", "Socks5"]


def gen_proxy_kb():
    proxies = proxytypes  # Copy, so that main list is not removed!
    kb = []
    while proxies:
        a = [
            InlineKeyboardButton(
                f"{proxies[0]}",
                callback_data=f"get_proxy.{proxies[0]}",
            )
        ]
        proxies.pop(0)
        if proxies:
            a.append(
                InlineKeyboardButton(
                    f"{proxies[0]}",
                    callback_data=f"get_proxy.{proxies[0]}",
                )
            )
            proxies.pop(0)
        kb.append(a)
    return kb


# Close button Query
@Client.on_callback_query(filters.regex("^close$"))
async def close_dialog_callback(c: Client, m: CallbackQuery):
    await m.message.delete()
    await m.message.reply_to_message.delete()
    await m.answer()
    return


# Get Http proxy Query
@Client.on_callback_query(filters.regex("^get_proxy."))
async def get_proxytype_callabcak(c: Client, m: CallbackQuery):
    me = await c.get_me()
    ptype = m.data.split(".")[1].lower()

    await m.message.edit_text(f"`Fetching {ptype} Proxies...`")

    proxygrab.save_proxy(ptype)  # Save proxies!

    caption = f"<b><i>Proxies scrapped by:</i></b> @{me.username}"
    filename = f"{ptype}_proxygrab.txt"

    await m.message.reply_document(document=filename, caption=caption)

    os.remove(filename)
    await m.message.reply_text(
        "If you'd like to keep this service alive 😊, please /donate"
    )
    await m.message.delete()
    await m.answer()


@Client.on_message(filters.command("proxies", COMMAND_HAND_LER))
async def get_proxies(c: Client, m: Message):

    await m.reply_text(
        "**__Which type of proxylist do you want?__**",
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                *gen_proxy_kb(),
                [InlineKeyboardButton("❌ Close", callback_data="close")],
            ]
        ),
    )

    return
