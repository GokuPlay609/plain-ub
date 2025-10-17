import random

from app import BOT, CustomDB, Message
from ub_core.utils import reply_and_delete

DARES = CustomDB["DARES"]


@BOT.add_cmd(cmd="dare")
async def dare(bot: BOT, message: Message):
    """
    CMD: DARE
    INFO: Get a random dare.
    USAGE: .dare
    """
    dares = await DARES.find_all()
    if not dares:
        await reply_and_delete(
            message, "No dares in the database. Add some with `.adddare`"
        )
        return

    dare = random.choice(dares)["text"]
    await message.edit_text(f"**Dare:** {dare}")


@BOT.add_cmd(cmd="adddare")
async def adddare(bot: BOT, message: Message):
    """
    CMD: ADDDare
    INFO: Add a dare to the database.
    USAGE: .adddare <dare>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to provide a dare to add.")
        return

    dare_text = message.text.split(maxsplit=1)[1]
    await DARES.add_data({"text": dare_text, "submitted_by": message.from_user.id})
    await reply_and_delete(message, "Dare added successfully.")