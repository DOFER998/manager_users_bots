import asyncio
import logging

import uvicorn
from beanie import init_beanie

from src import (
    get_handlers_router,
    info_controller,
    remove_commands,
    start_logging,
    set_commands,
    SelfBotModal,
    UserModel,
    InfoModel,
    db_client,
    bot,
    dp,
)


async def on_startup():
    dp.include_router(get_handlers_router())
    await init_beanie(
        database=db_client.Bot,
        document_models=[
            SelfBotModal,
            InfoModel,
            UserModel
        ],
        multiprocessing_mode=True
    )
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await info_controller.create()

    logging.error('Bot started!')


async def on_shutdown():
    logging.warning('Stopping bot...')
    await remove_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.fsm.storage.close()
    await bot.session.close()


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        logger: logging.RootLogger = start_logging()
        asyncio.run(main(), debug=True)
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
