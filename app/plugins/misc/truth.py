import random

from app import BOT, Message
from app.core.db.models import Truths
from ub_core.utils import reply_and_delete


@BOT.add_cmd(cmd="truth")
async def truth(bot: BOT, message: Message):
    """
    CMD: TRUTH
    INFO: Get a random truth question.
    USAGE: .truth
    """
    truths = await Truths.all()
    if not truths:
        await reply_and_delete(message, "No truths in the database. Add some with `.addtruth`")
        return

    truth = random.choice(truths).text
    await message.edit_text(f"**Truth:** {truth}")


@BOT.add_cmd(cmd="addtruth")
async def addtruth(bot: BOT, message: Message):
    """
    CMD: ADDTRUTH
    INFO: Add a truth to the database.
    USAGE: .addtruth <truth>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to provide a truth to add.")
        return

    truth_text = message.text.split(maxsplit=1)[1]
    await Truths.create(text=truth_text, submitted_by=message.from_user.id)
    await reply_and_delete(message, "Truth added successfully.")