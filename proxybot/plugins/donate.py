from pyrogram import Client, filters

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from proxybot import COMMAND_HAND_LER, CONTACT_OWNER

close_btn_reply_markup = [[InlineKeyboardButton("❌ Close", callback_data="close")]]
DONATE_TEXT = """
Glad you'd like to donate!

You can donate my Owner by contacting him >>> @{} \
If you donate, the number of proxies may increase \
and it would also motivate my developer to maintain \
his hobbies such as building bots!
"""


@Client.on_message(filters.command("donate", COMMAND_HAND_LER))
async def donate_owner(c: Client, m: Message):

    user_name = m.from_user.first_name

    await m.reply_text(
        DONATE_TEXT.format(CONTACT_OWNER),
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(close_btn_reply_markup),
    )
    return
