import asyncio
import importlib
from pyrogram import idle
from Xiao import LOGGER, app, start_bot
from Xiao.plugins import ALL_MODULES
from Xiao.core.chat_tracker import verify_groups_command
from Xiao.core.clone import restart_bots
from config import OWNER_ID

class DummyUser:
    id = OWNER_ID

class DummyMessage:
    from_user = DummyUser()

    async def reply_text(self, *args, **kwargs):
        pass

async def init():
    await restart_bots()
    await start_bot()

    for all_module in ALL_MODULES:
        importlib.import_module("Xiao.plugins" + all_module)
    LOGGER("Xiao.plugins").info("✅ Successfully imported all modules.")

    try:
        dummy_message = DummyMessage()
        await verify_groups_command(app, dummy_message)
        LOGGER("Xiao").info("🔁 Automatically verified groups on startup.")
    except Exception as e:
        LOGGER("Xiao").warning(f"⚠️ Failed to verify groups on startup: {e}")

    LOGGER("Xiao").info("🚀 Xiao Music bot Started Successfully.")
    await idle()

    await app.stop()
    LOGGER("Xiao").info("🛑 Stopping Xiao Music bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())