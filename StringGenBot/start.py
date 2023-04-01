from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
This is a string session boat. In this you can create your own string session. Here you are completely secure. No danger to your string session here./n/n
-.-.-.-.-.-.-.-.-.||/n/n
यह एक स्ट्रिंग सेशन बोट है। इसमें आप अपना खुद का स्ट्रिंग सेशन बना सकते हैं। यहां आप पूरी तरह सुरक्षित हैं। यहां आपके स्ट्रिंगसेशन को कोई खतरा नहीं है।
/n/n-.-.-.-.-.-.-.-.-.||
©️ ʙʏ : [𝐁𝐋𝐀𝐂𝐊𝐌𝐀𝐌𝐁𝐀](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🥰 🄶🄴🄽🄴🅁🄰🅃🄴 🅈🄾🅄🅁 🄾🅆🄽 🅂🄴🅂🅂🄸🄾🄽 🥰", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" ✌️ 🄹🄾🄸🄽 ✌️ ", url="https://t.me/GORILLA_NETWORK"),
                    InlineKeyboardButton("😎 🄾🅆🄽🄴🅁 😎 ", url="https://t.me/MAMBA_RETURNS")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
