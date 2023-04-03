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

𝐓𝐡𝐢𝐬 𝐢𝐬 {me2},
𝐓𝐡𝐢𝐬 𝐢𝐬 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐛𝐨𝐭. 𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐰𝐫𝐢𝐭𝐭𝐞𝐧 𝐢𝐧 𝐏𝐲𝐭𝐡𝐨𝐧 𝐰𝐢𝐭𝐡 𝐭𝐡𝐞 𝐡𝐞𝐥𝐩 𝐨𝐟 𝐏𝐲𝐭𝐡𝐨𝐧. 𝐈𝐧 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐨𝐩𝐭𝐢𝐨𝐧 𝐰𝐡𝐢𝐜𝐡 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭.......

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝔐𝔞𝔪𝔟𝔞](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=" 💥 𝘉𝘶𝘪𝘭𝘥 𝘺𝘰𝘶𝘳 𝘚𝘦𝘴𝘴𝘪𝘰𝘯 💥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" 🥰 ѕσυя¢є ", url="https://pornhub.com"),
                    InlineKeyboardButton("😎∂єνєℓσρєя😎", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
