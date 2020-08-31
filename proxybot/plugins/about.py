import platform
from pyrogram import __version__, Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)
from proxybot import COMMAND_HAND_LER, BOT_VERSION, OWNER_ID

about_me_text = """
<b>Creator:</b> <a href='tg://user?id={}'>{}</a>
<b>Credits:</b> <a href='https://t.me/haskell'>Dan</a> for his pyrogram library, each and everyone who made this project possible!
<b>Made using:</b> <a href='https://python.org'>Python v{}</a>
<b>Library:</b> <a href='https://docs.pyrogram.org'>Pyrogram v{}</a>
<b>Server:</b> <a href='https://heroku.com'>Heroku</a>
<b>Build Status:</b> <i>v{}</i>

<b>Bot Username:</b> @{}

<b>Request: </b>Please don't spam bot, if the API reaches its limit, bot will be unusable!
"""


@Client.on_message(filters.command("about", COMMAND_HAND_LER))
async def about_owner(c: Client, m: Message):

    get_owner = await c.get_users(OWNER_ID)
    me = await c.get_me()

    keyboard_about = [[InlineKeyboardButton("❌ Close", callback_data="close")]]

    await m.reply_text(
        about_me_text.format(
            get_owner.id,
            get_owner.first_name,
            platform.python_version(),
            __version__,
            BOT_VERSION,
            me.username,
        ),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(keyboard_about),
    )
    return
