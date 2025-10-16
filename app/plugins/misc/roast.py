import random

from app import BOT, Message
from app.core.db.models import Roasts
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="roast")
async def roast(bot: BOT, message: Message):
    """
    CMD: ROAST
    INFO: Deliver a random roast to a user.
    USAGE: .roast <reply/username>
    """
    user, _ = await extract_user(bot, message)
    if not user:
        await reply_and_delete(message, f"I can't find that user.")
        return

    roasts = await Roasts.all()
    if not roasts:
        await reply_and_delete(message, "No roasts in the database. Add some with `.addroast`")
        return

    roast = random.choice(roasts).text
    await message.edit_text(f"{user.mention}, {roast}")


@BOT.add_cmd(cmd="addroast")
async def addroast(bot: BOT, message: Message):
    """
    CMD: ADDROAST
    INFO: Add a roast to the database.
    USAGE: .addroast <roast>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to provide a roast to add.")
        return

    roast_text = message.text.split(maxsplit=1)[1]
    await Roasts.create(text=roast_text, submitted_by=message.from_user.id)
    await reply_and_delete(message, "Roast added successfully.")