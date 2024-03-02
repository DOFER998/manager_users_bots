from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class SelfBotModal(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    api_id: int
    api_hash: str
    session_string: str

    class Settings:
        name = 'self_bots'
