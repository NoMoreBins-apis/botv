from pyrogram import Client, filters
from FUNC.usersdb_func import *
import httpx
from TOOLS.check_all_func import *


@Client.on_message(filters.command("bin", [".", "/"]))
async def cmd_bin(Client, message):
    try:
        user_id, chat_type, chat_id = (
            str(message.from_user.id),
            str(message.chat.type),
            str(message.chat.id),
        )
        checkall = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            bin = message.text.split(" ")[1]
        except:
            resp = f"""<b>
Invalid BIN ⚠️

Message: Not Found Any Valid BIN From Your Input .
            </b>"""
            await message.reply_text(resp, message.id)
            return

        fbin = bin[:6]
        session = httpx.AsyncClient()
        try:
            bin = await session.get(f"https://lookup.binlist.net/{fbin}").json()
        except:
            bin = "N/A"
        try:
            brand = bin["scheme"].upper()
        except:
            brand = "N/A"
        try:
            type = bin["type"].upper()
        except:
            type = "N/A"
        try:
            level = bin["brand"].upper()
        except:
            level = "N/A"
        try:
            bank_data = bin["bank"]
        except:
            bank_data = "N/A"
        try:
            bank = bank_data["name"].upper()
        except:
            bank = "N/A"
        try:
            country_data = bin["country"]
        except:
            country_data = "N/A"
        try:
            country = country_data["name"].upper()
        except:
            country = "N/A"
        try:
            flag = country_data["emoji"]
        except:
            flag = "N/A"
        try:
            currency = country_data["currency"].upper()
        except:
            currency = "N/A"
        resp = f"""<b>
BIN Info Fetched Successfully ✅
━━━━━━━━━━━━━━ 
Status : Valid 
BIN:  <code>{fbin}</code> 
Brand: {brand} 
Level: {level} 
Type: {type} 
Bnak: {bank} 
Country: {country} - {flag} - {currency} 

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
</b>"""
        await message.reply_text(resp, message.id)
        await session.aclose()

    except:
        import traceback
        await error_log(traceback.format_exc())
