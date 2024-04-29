import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import Bot
from config import ADMINS, FORCE_MSG

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    if len(message.command) > 1:
        buttons = [
            [
                InlineKeyboardButton(
                    "Join EonixCore",
                    url="https://t.me/EonixCore"),
                InlineKeyboardButton(
                    "Join BontenCriminals",
                    url="https://t.me/BontenCriminals")
            ],
            [
                InlineKeyboardButton(
                    "Join AC Anime Group",
                    url="https://t.me/AC_Anime_Group")
            ],
            [
                InlineKeyboardButton(
                    text='Try Again',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        ]

        await message.reply(
            text=FORCE_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
            disable_web_page_preview=True
        )
    else:
        # Handle case when command has no arguments
        await message.reply("Please provide valid arguments with the command.")
