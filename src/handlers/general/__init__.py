from aiogram import Router


def get_general_router() -> Router:
    from . import start, self_bot, mailing

    router = Router()

    router.include_router(start.router)
    router.include_router(self_bot.router)
    router.include_router(mailing.router)

    return router
