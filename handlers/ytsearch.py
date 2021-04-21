# GalaxyMusic (Telegram bot project )
# Copyright (C) 2021  Prabhasha 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



# the logging things
import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["yts"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/yts `Your KeyWord`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜 •••")
        results = YoutubeSearch(query, max_results=8).to_dict()
        i = 0
        text = ""
        while i < 8:
            text += f"𝙏𝙞𝙩𝙡𝙚  ⛓- {results[i]['title']}\n"
            text += f"𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣  ⏳- {results[i]['duration']}\n"
            text += f"𝙑𝙞𝙚𝙬𝙨  👀- {results[i]['views']}\n"
            text += f"𝘾𝙝𝙖𝙣𝙣𝙚𝙡  📺- {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
