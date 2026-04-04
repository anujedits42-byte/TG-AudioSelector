# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.enums import ChatAction, ParseMode
import asyncio
import random
import logging
from utils import safe_telegram_call
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
logger = logging.getLogger(__name__)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# Sticker and images
START_PIC = "https://telegra.ph/HgBotz-08-09-5"
ABOUT_PIC = "https://telegra.ph/HgBotz-08-09-6"
stickers = [
    "CAACAgUAAxkBAAEOXBhoCoKZ76jevKX-Vc5v5SZhCeQAAXMAAh4KAALJrhlVZygbxFWWTLw2BA"
]
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
welcome_text = "<i><blockquote>Wᴇʟᴄᴏᴍᴇ, ʙᴀʙʏ… ɪ’ᴠᴇ ʙᴇᴇɴ ᴄʀᴀᴠɪɴɢ ʏᴏᴜʀ ᴘʀᴇsᴇɴᴄᴇ ғᴇᴇʟs ᴘᴇʀғᴇᴄᴛ ɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ’ʀᴇ ʜᴇʀᴇ.</blockquote></i>"
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
def create_main_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/log_channel_a"),
        ],
        [
            InlineKeyboardButton("Dᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/anujedits76"),
        ],
    ])
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
def register_start_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start_cmd(client: Client, message: Message):
        # Animated intro
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        msg = await message.reply_text(welcome_text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await msg.edit_text("<b><i><pre>Sᴛᴀʀᴛɪɴɢ...</pre></i></b>", parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await msg.delete()

        # Sticker
        await client.send_chat_action(message.chat.id, ChatAction.CHOOSE_STICKER)
        await message.reply_sticker(random.choice(stickers))

        # Main message
        caption = (
            f"<pre>Hᴇʏ ᴄᴜᴛɪᴇ</pre>\n"
            f"<b><blockquote>›› ɪ’ᴍ ᴀ ʜᴀɴᴅʏ ᴀᴜᴅɪᴏ ꜱᴇʟᴇᴄᴛᴏʀ ʙᴏᴛ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ ᴏʀ ʀᴇᴍᴏᴠᴇ ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋꜱ ꜰʀᴏᴍ ʏᴏᴜʀ ᴠɪᴅᴇᴏꜱ!</b></blockquote>\n"
            f"<b><blockquote>◈ <a href='https://t.me/anujedits76'>𝐀𝐍𝐔𝐉 𝐊𝐔𝐌𝐀𝐑</a></b></blockquote>"
        )

        if START_PIC:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=START_PIC,
                caption=caption,
                reply_markup=create_main_buttons(),
                parse_mode=ParseMode.HTML
            )
        else:
            await app.send_message(
                chat_id=message.chat.id,
                text=caption,
                reply_markup=create_main_buttons(),
                parse_mode=ParseMode.HTML
            )
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_callback_query(filters.regex("about"))
    async def about_cb(client: Client, callback_query):
        about_buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
            ]
        ])

        about_caption = (
            "<b><blockquote>Hᴇʏ ᴅᴇᴀʀ ᴍʏ ɴᴀᴍᴇ 𝐀𝐍𝐔𝐉 𝐊𝐔𝐌𝐀𝐑</b></blockquote>\n"
            f"<b><blockquote>◈ Oᴡɴᴇʀ : <a href='https://t.me/anujedits76'>𝐀𝐍𝐔𝐉 𝐊𝐔𝐌𝐀𝐑</a>\n"
            f"◈ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='https://t.me/anujedits76'>𝐀𝐍𝐔𝐉</a>\n"
            f"◈ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href='https://t.me/log_channel_a'>𝐀𝐊</a>\n"
            f"◈ Uᴩᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ : <a href='https://t.me/log_channel_a'>𝐀𝐊</a></b></blockquote>"
        )

        await callback_query.message.edit_media(
            media=InputMediaPhoto(media=ABOUT_PIC, caption=about_caption, parse_mode=ParseMode.HTML),
            reply_markup=about_buttons
        )
        await callback_query.answer()

    @app.on_callback_query(filters.regex("close"))
    async def close_cb(client: Client, callback_query):
        try:
            await callback_query.message.delete()
        except Exception:
            pass
        await callback_query.answer("Closed.")

    @app.on_callback_query(filters.regex("back"))
    async def back_cb(client: Client, callback_query):
        main_caption = (
            f"<pre>Hᴇʏ ᴄᴜᴛɪᴇ</pre>\n"
            f"<b><blockquote>›› I’ᴍ ᴀ ᴄᴜᴛᴇ ᴀɴɪᴍᴇ ɴᴇᴡs ʙᴏᴛ ᴍᴀᴅᴇ ᴛᴏ sʜᴀʀᴇ ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴜᴘᴅᴀᴛᴇs ᴡɪᴛʜ ʏᴏᴜʀ sᴘᴇᴄɪᴀʟ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ</b></blockquote>\n"
            f"<b><blockquote>◈ <a href='https://t.me/anujedits76'>𝐀𝐍𝐔𝐉</a></b></blockquote>"
        )

        if START_PIC:
            await callback_query.message.edit_media(
                media=InputMediaPhoto(media=START_PIC, caption=main_caption, parse_mode=ParseMode.HTML),
                reply_markup=create_main_buttons()
            )
        else:
            await callback_query.message.edit_text(
                text=main_caption,
                reply_markup=create_main_buttons(),
                parse_mode=ParseMode.HTML
            )
        await callback_query.answer()
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
