from tortoise import fields
from tortoise.models import Model


class Dares(Model):
    """
    Tortoise ORM Model for Dares
    """

    id = fields.IntField(pk=True)
    text = fields.TextField()
    submitted_by = fields.BigIntField()

    class Meta:
        table = "dares"