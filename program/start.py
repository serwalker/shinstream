from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Allows you to play music and video on groups through the new Telegram's video chats!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❓ Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("📣 Support", url=f"https://t.me/{GROUP_SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **Thanks for adding me to the Group !**\n\n"
                "**Promote me as administrator of the Group, otherwise I will not be able to work properly, and don't forget to type /userbotjoin for invite the assistant.**\n\n"
                "**Once done, type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("👥 Support", url=f"https://t.me/{GROUP_SUPPORT}")
                        ]
                    ]
                )
            )
