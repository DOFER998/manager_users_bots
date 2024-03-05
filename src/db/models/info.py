from beanie import Document


class InfoModel(Document):
    id: int
    info: str
    version: str

    class Settings:
        name = 'info'
