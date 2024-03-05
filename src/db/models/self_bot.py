from beanie import Document


class SelfBotModal(Document):
    id: int
    name: str
    api_id: int
    api_hash: str
    session_string: str

    class Settings:
        name = 'self_bots'
