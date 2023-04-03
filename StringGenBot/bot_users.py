from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from StringGenBot.db.users import add_served_user, get_served_users


@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ℭ𝔲𝔯𝔯𝔢𝔫𝔱 𝔰𝔱𝔞𝔱𝔲𝔰 𝔬𝔣 𝔖𝔱𝔯𝔦𝔫𝔤 𝔖𝔢𝔰𝔰𝔦𝔬𝔫 𝔊𝔢𝔫𝔢𝔯𝔞𝔱𝔬𝔯 𝔅𝔬𝔱 𝔦𝔰 :\n\n {users} 𝔲𝔰𝔢𝔯𝔰", quote=True)
