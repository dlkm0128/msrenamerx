import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"𝙾𝚛𝚒𝚐𝚒𝚘𝚗𝚊𝚕 𝙱𝙾𝚃 :- <a href='https://t.me/Kali_Rename_Bot'>𝐊𝐚𝐥𝐢 𝐑𝐞𝐧𝐚𝐦𝐞𝐫 𝐁𝐨𝐭</a>\n𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 :- <a href='https://t.me/Kalitgadmin_Bot'>🧑🏻‍🦱𝐊𝐚𝐥𝐢🕊️ ⃟⃟⃝⃪⃟⃝🦋─⃛͢🧑🏻‍🦱</a>\n𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 :- 𝙿𝚢𝚝𝚑𝚘𝚗𝟹\n𝙻𝚒𝚋𝚛𝚊𝚛𝚢 :- 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 𝟸.𝟶\n𝚂𝚎𝚛𝚟𝚎𝚛 :- 𝚁𝚎𝚗𝚍𝚎𝚛\n𝚃𝚘𝚝𝚊𝚕 𝚁𝚎𝚗𝚊𝚖𝚎𝚍 𝙵𝚒𝚕𝚎 :- {total_rename}\n𝚃𝚘𝚝𝚊𝚕 𝚂𝚒𝚣𝚎 𝚁𝚎𝚗𝚊𝚖𝚎𝚍 :- {humanbytes(int(total_size))}\n\n 𝚃𝚑𝚊𝚗𝚔 𝚢𝚘𝚞 **<a href='https://t.me/Kalitgadmin_Bot'>𝐊𝐚𝐥𝐢🕊️ ⃟⃟⃝⃪⃟⃝🦋─⃛͢</a>** 𝚏𝚘𝚛 𝚢𝚘𝚞𝚛 𝚑𝚊𝚛𝚍 𝚠𝚘𝚛𝚔",quote=True)
