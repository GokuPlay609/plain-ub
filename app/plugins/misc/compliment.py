import random

from app import BOT, Message
from app.core.db.models import Compliments
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="compliment")
async def compliment(bot: BOT, message: Message):
    """
    CMD: COMPLIMENT
    INFO: Deliver a random compliment to a user.
    USAGE: .compliment <reply/username>
    """
    user, _ = await extract_user(bot, message)
    if not user:
        await reply_and_delete(message, f"I can't find that user.")
        return

    compliments = await Compliments.all()
    if not compliments:
        await reply_and_delete(message, "No compliments in the database. Add some with `.addcompliment`")
        return

    compliment = random.choice(compliments).text
    await message.edit_text(f"{user.mention}, {compliment}")


@BOT.add_cmd(cmd="addcompliment")
async def addcompliment(bot: BOT, message: Message):
    """
    CMD: ADDCOMPLIMENT
    INFO: Add a compliment to the database.
    USAGE: .addcompliment <compliment>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to provide a compliment to add.")
        return

    compliment_text = message.text.split(maxsplit=1)[1]
    await Compliments.create(text=compliment_text, submitted_by=message.from_user.id)
    await reply_and_delete(message, "Compliment added successfully.")