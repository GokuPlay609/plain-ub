from tortoise import fields
from tortoise.models import Model


class Slaps(Model):
    """
    Tortoise ORM Model for Slap Stats
    """

    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    slapped_count = fields.IntField(default=0)
    slapped_by_count = fields.IntField(default=0)

    class Meta:
        table = "slaps"