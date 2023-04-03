from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/e685702e02bf7a76e8a81.jpg", caption=f"» ǟƈƈօʀɖɨռɢ ȶօ ʍʏ ɖǟȶǟɮǟֆɛ, ʏօʊ ɦǟʋɛ ռօȶ ʝօɨռɛɖ [🄶🄾🅁🄸🄻🄻🄰]({link}) ʏɛȶ, ɨʄ ʏօʊ աǟռȶ ȶօ ʊֆɛ ʍɛ ȶɦɛռ ƈʟɨƈӄ օռ ʝօɨռ ɮʊȶȶօռ [🄶🄾🅁🄸🄻🄻🄰]({link}) ǟռɖ ǟʄȶɛʀ ʝօɨռ, ȶɦɛռ ʏօʊ ֆȶǟʀȶ ʍɛ ǟɢǟɨռ !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> 🄶🄾🅁🄸🄻🄻🄰", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"𝔓𝔯𝔬𝔪𝔬𝔱𝔢 𝔪𝔢 𝔞𝔰 𝔞 𝔞𝔡𝔪𝔦𝔫 𝔦𝔫 𝔱𝔥𝔢 MUST_JOIN 𝔠𝔥𝔞𝔱 : {MUST_JOIN} !")
