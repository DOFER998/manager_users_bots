from aiogram import Router


def get_owner_router() -> Router:
    from . import reset_commands, utils_admin

    router = Router()

    router.include_router(reset_commands.router)
    router.include_router(utils_admin.router)

    return router
