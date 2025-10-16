from tortoise import fields
from tortoise.models import Model


class Roasts(Model):
    """
    Tortoise ORM Model for Roasts
    """

    id = fields.IntField(pk=True)
    text = fields.TextField()
    submitted_by = fields.BigIntField()

    class Meta:
        table = "roasts"