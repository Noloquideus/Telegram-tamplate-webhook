import config
from aiogram import Bot, Dispatcher, types
from aiohttp import web

# Инициализация бота
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет! Я ваш Telegram-бот.")

# Функция для настройки вебхука
async def on_startup(dp):
    webhook_url = config.WEBHOOK_URL
    await bot.set_webhook(webhook_url)

# Функция для остановки вебхука
async def on_shutdown(dp):
    await bot.delete_webhook()

# Запуск бота как веб-приложения
if __name__ == '__main__':
    from aiogram import executor
    from aiogram.dispatcher.webhook import get_new_configured_app

    app = get_new_configured_app(dispatcher=dp, path=f'/{config.BOT_TOKEN}')
    executor.start_webhook(
        dp,
        app=app,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
