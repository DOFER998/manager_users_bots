from aiogram import Router


def get_handlers_router() -> Router:
    from src.handlers.general import get_general_router
    from src.handlers.owner import get_owner_router

    router = Router()

    general_router = get_general_router()
    owner_router = get_owner_router()

    router.include_router(general_router)
    router.include_router(owner_router)

    return router
