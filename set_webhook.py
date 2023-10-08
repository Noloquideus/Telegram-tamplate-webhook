import asyncio
import logging
import config
from aiogram import Bot

bot = Bot(token=config.BOT_TOKEN)

async def set_webhook():
    webhook_url = config.WEBHOOK_URL
    await bot.set_webhook(webhook_url)

if __name__ == '__main__':
    from aiogram import executor

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhook())
