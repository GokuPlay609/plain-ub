from tortoise import fields
from tortoise.models import Model


class Truths(Model):
    """
    Tortoise ORM Model for Truths
    """

    id = fields.IntField(pk=True)
    text = fields.TextField()
    submitted_by = fields.BigIntField()

    class Meta:
        table = "truths"