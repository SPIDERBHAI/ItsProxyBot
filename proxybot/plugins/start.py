import os
from pyrogram import (
    Client,
    filters,
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message,
)
from proxybot import COMMAND_HAND_LER, AUTH_GROUP_USERNAME

# -- Constants -- #
close_btn_reply_markup = [[InlineKeyboardButton("❌ Close", callback_data="close")]]
START_TEXT = """
Hey {}

I'm @{}, to provide you with proxies!
I'll fetch proxies from different sites \
and give you here as a file.

Source Code - (Github)[https://github.com/Skuzzers/ItsProxyBot]

__**Made with ❤️ in India**__
"""

HELP_TEXT = f"""
{COMMAND_HAND_LER}start - Show Start message.
{COMMAND_HAND_LER}help - Check this help message.
{COMMAND_HAND_LER}proxies - Show a inline menu to choose which proxies to download.
{COMMAND_HAND_LER}about - Get information about me
{COMMAND_HAND_LER}donate - Get information about donating my owner.
"""
# -- Constants End -- #


# -- Bot Function starts -- #
@Client.on_message(filters.command("start", COMMAND_HAND_LER))
async def start_bot(c: Client, m: Message):
    me = await c.get_me()

    keyboard_start = [
        [
            InlineKeyboardButton("How to use?", callback_data="help_callback"),
            InlineKeyboardButton(
                "Help & Support", url="https://t.me/{}".format(AUTH_GROUP_USERNAME)
            ),
        ]
    ]
    user = m.from_user.first_name
    await m.reply_text(
        START_TEXT.format(user, me.username),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(keyboard_start),
    )
    return


# Start-Help button Query
@Client.on_callback_query(filters.regex("^help_callback$"))
async def help_bot_callback(c: Client, q: CallbackQuery):
    await q.message.edit_text(
        HELP_TEXT,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(close_btn_reply_markup),
    )
    await q.answer()


@Client.on_message(filters.command("help", COMMAND_HAND_LER))
async def help_bot(c: Client, m: Message):

    await m.reply_text(
        HELP_TEXT,
        parse_mode="markdown",
        reply_to_message_id=m.message_id,
        reply_markup=InlineKeyboardMarkup(close_btn_reply_markup),
    )

    return
