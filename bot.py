import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config.settings import TELEGRAM_TOKEN, ADMIN_ID
from core.logic.brain import TitanBrain

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
titan = TitanBrain()

# AUTH CHECK
def is_auth(user_id):
    return ADMIN_ID == 0 or user_id == ADMIN_ID

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("🧬 **TITAN OMEGA v∞⁸ ONLINE**\nHuman-Grade Logic Hunter\n\n/scan <target>\n/stop\n/resume\n/status")

@dp.message(Command("scan"))
async def scan(msg: types.Message):
    if not is_auth(msg.from_user.id): return
    args = msg.text.split()
    if len(args) < 2: return await msg.answer("Usage: /scan target.com")
    
    status_msg = await msg.answer(f"🚀 **Target Acquired:** `{args[1]}`")

    # Logger callback to allow Brain to update Telegram
    async def logger(text):
        try: await status_msg.edit_text(text)
        except: pass

    # Run the brain
    report = await titan.start_scan(args[1], logger)
    
    if report:
        await msg.answer_document(FSInputFile(report), caption="🔥 **CRITICAL LOGIC BUG FOUND**")
    else:
        await msg.answer("🏁 **Scan Finished.** No Critical Logic Bugs found.")

@dp.message(Command("stop"))
async def stop(msg: types.Message):
    if not is_auth(msg.from_user.id): return
    titan.is_active = False
    await msg.answer("🛑 **Stopping... State Saved.**")

@dp.message(Command("status"))
async def status(msg: types.Message):
    state = "Active" if titan.is_active else "Idle"
    await msg.answer(f"📊 **System Status:** {state}")

@dp.message(Command("shutdown"))
async def shutdown(msg: types.Message):
    if not is_auth(msg.from_user.id): return
    await msg.answer("🔌 **Shutting down...**")
    await bot.session.close()
    exit()

# ENTRY
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
