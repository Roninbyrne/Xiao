import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, OWNER_ID, GROUPS_TO_JOIN
from Xiao import app as bot
from Xiao.core.mongo import mongo_collection

@bot.on_message(filters.command("clone") & filters.private)
async def on_clone(client, message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        string_token = message.command[1]

        existing_bot = await mongo_collection.find_one({"string": string_token})
        if existing_bot:
            await message.reply_text(
                "➢ ᴛʜɪs Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ. Use /startub if it's off."
            )
            return

        ai = Client(
            f"{user_name}",
            API_ID,
            API_HASH,
            session_string=string_token,
            plugins={"root": "Xiao.plugins.core.clone"},
        )

        await ai.start()
        for chat in GROUPS_TO_JOIN:
            await ai.join_chat(chat)

        bot_info = await ai.get_me()

        details = {
            "is_bot": False,
            "user_id": user_id,
            "name": bot_info.first_name,
            "string": string_token,
            "username": bot_info.username,
        }

        await mongo_collection.insert_one(details)

        await message.reply_text(
            f"<b>Successfully cloned your Assistant UserBot: @{bot_info.username}.\n"
            f"Start the bot using `.start`. For help, type `.help`.</b>"
        )
    except BaseException as e:
        logging.exception(f"Error while cloning ub: {e}")
        await message.reply_text(
            f"⚠️ <b>Assistant UserBot Error:</b>\n\n<code>{e}</code>\n\n"
            "**Kindly forward this message to the owner to get assistance.**"
        )

@bot.on_message(filters.command("deleteclone") & filters.private)
async def delete_cloned_bot(client, message):
    try:
        if message.reply_to_message:
            string_token = message.reply_to_message.text.strip()
        elif len(message.command) > 1:
            string_token = message.text.split(None, 1)[1].strip()
        else:
            await message.reply_text(
                "➢ Send this command with your Assistant session.\nExample: /deleteclone <your session>"
            )
            return

        cloned_bot = await mongo_collection.find_one({"string": string_token})
        if cloned_bot:
            await mongo_collection.delete_one({"string": string_token})
            await message.reply_text(
                "➢ The cloned Assistant UserBot has been removed and deleted from the database."
            )
        else:
            await message.reply_text("No matching session found in the database.")
    except Exception as e:
        logging.exception(f"Error while deleting cloned Assistant: {e}")
        await message.reply_text("An error occurred while deleting the Assistant.")

async def restart_bots():
    logging.info("Restarting all clients...")
    bots = mongo_collection.find()
    async for bot in bots:
        string_token = bot["string"]
        try:
            ai = Client(
                f"{string_token}",
                API_ID,
                API_HASH,
                session_string=string_token,
                plugins={"root": "ComboBot.plugins.userbot"},
            )
            await ai.start()
            for chat in GROUPS_TO_JOIN:
                await ai.join_chat(chat)
        except Exception as e:
            logging.exception(f"Error while restarting assistant: {e}")

@bot.on_message(filters.command("allclient", ".") & filters.user(OWNER_ID))
async def akll(_, message):
    bots = mongo_collection.find()
    all_client = "All clients:\n"
    async for bot in bots:
        all_client += f"{bot['user_id']} : {bot['name']}\n"
    await message.reply(all_client)