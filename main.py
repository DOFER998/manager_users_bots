import asyncio
import logging

from beanie import init_beanie

from src import (
    get_handlers_router,
    info_controller,
    remove_commands,
    set_commands,
    SelfBotModal,
    UserModel,
    InfoModel,
    db_client,
    bot,
    app,
    dp,
)


@app.on_event('startup')
async def on_startup():
    dp.include_router(get_handlers_router())
    await bot.delete_webhook(drop_pending_updates=True)
    await init_beanie(
        database=db_client.Bot,
        document_models=[
            SelfBotModal,
            InfoModel,
            UserModel
        ]
    )
    await set_commands(bot)
    await info_controller.create()

    logging.error('Bot started!')


@app.on_event('shutdown')
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
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
