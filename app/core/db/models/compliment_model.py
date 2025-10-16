from tortoise import fields
from tortoise.models import Model


class Compliments(Model):
    """
    Tortoise ORM Model for Compliments
    """

    id = fields.IntField(pk=True)
    text = fields.TextField()
    submitted_by = fields.BigIntField()

    class Meta:
        table = "compliments"