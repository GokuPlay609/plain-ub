from tortoise import fields
from tortoise.models import Model


class Ships(Model):
    """
    Tortoise ORM Model for Ships
    """

    id = fields.IntField(pk=True)
    user1_id = fields.BigIntField()
    user2_id = fields.BigIntField()
    ship_name = fields.CharField(max_length=255)

    class Meta:
        table = "ships"
        unique_together = (("user1_id", "user2_id"),)