import random

from app import BOT, Message
from app.core.db.models import Ships
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="ship")
async def ship(bot: BOT, message: Message):
    """
    CMD: SHIP
    INFO: Ship two users together and generate a ship name.
    USAGE: .ship <reply/username> <reply/username>
    """
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await reply_and_delete(
            message, "Reply to a user's message to ship them with another user."
        )
        return

    user1 = message.reply_to_message.from_user
    user2, _ = await extract_user(bot, message)

    if not user2:
        await reply_and_delete(message, "I can't find the second user.")
        return

    if user1.id == user2.id:
        await reply_and_delete(message, "You can't ship a user with themselves.")
        return

    ship_name = user1.first_name[: len(user1.first_name) // 2] + user2.first_name[
        len(user2.first_name) // 2 :
    ]
    await Ships.get_or_create(
        user1_id=user1.id, user2_id=user2.id, defaults={"ship_name": ship_name}
    )
    await message.edit_text(f"I ship {user1.mention} and {user2.mention}! Ship name: **{ship_name}**")