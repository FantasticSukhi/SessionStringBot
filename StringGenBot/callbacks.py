import traceback

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from StringGenBot.generate import generate_session, ask_ques, buttons_ques


@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram_bot":
                await callback_query.answer("» тнє ѕєѕѕιση gєηєяαтσя ωιℓℓ вє σƒ ρуяσgяαм ν2.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "𝚆𝚑𝚊𝚝𝚜 𝚝𝚑𝚎 𝚑𝚎𝚕𝚕 !!!! 𝚂𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 𝚠𝚎𝚗𝚝 𝚠𝚛𝚘𝚗𝚐. \𝚗\𝚗**𝙴𝚛𝚛𝚘𝚛**:{} "\
                "\𝚗\𝚗**𝙿𝚕𝚎𝚊𝚜𝚎 𝚏𝚘𝚛𝚠𝚊𝚛𝚍 𝚝𝚑𝚒𝚜 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 @𝙶𝙾𝚁𝙸𝙻𝙻𝙰_𝙱𝙾𝚃𝚂**, 𝙸𝚏 𝚝𝚑𝚒𝚜 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 "\
                "𝚍𝚘𝚎𝚜𝚗'𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗 𝚊𝚗𝚢 𝚜𝚎𝚗𝚜𝚒𝚒𝚟𝚎 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 "\
                "𝚋𝚎𝚌𝚊𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚎𝚛𝚛𝚘𝚛 𝚒𝚜 𝚕𝚘𝚐𝚐𝚎𝚍 𝚋𝚢 𝚝𝚑𝚎 𝚋𝚘𝚝** !!!!"
