from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://ibb.co/KzqGkR7",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[ᑕᕼE GᑌEᐯᗩᖇᗩ](https://t.me/Venom_is_alive)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    
                    [
                        InlineKeyboardButton("𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍", url='https://t.me/Venom_is_alive'),
                        InlineKeyboardButton("𝙈𝙊𝙑𝙄𝙀 𝘽𝙊𝙏", url='https://t.me/Moviesvenubot')
                    ]
                ]
            )
        )
  
