from pyrogram import Client, filters
import random


@Client.on_message(filters.command("gay", [".", "/"]))
async def cmd_id(Client, message):
    try:
        user_id = str(message.from_user.id)
        if user_id == "5371579102":
            gayness = "0"
        else:
            gayness = random.randint(0, 100)

        if message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            if user_id == "5371579102":
                gayness = "0"
            else:
                gayness = random.randint(0, 100)
            texta = f"""
Hey <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !

You will be Happy to Know That You are <b>{gayness}%</b> Gay 😀😀
    """
            await message.reply_text(texta, message.id)

        else:
            texta = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !

You will be Happy to Know That You are <b>{gayness}%</b> Gay 😀😀
      """
            await message.reply_text(texta, message.id)
            
    except:
        pass
