import random

from app import BOT, Message
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="love")
async def love(bot: BOT, message: Message):
    """
    CMD: LOVE
    INFO: Calculate a love compatibility score between two users.
    USAGE: .love <username1> <username2>
    """
    if len(message.cmd) != 3:
        await reply_and_delete(message, "Usage: .love <username1> <username2>")
        return

    user1, _ = await extract_user(bot, message, 1)
    user2, _ = await extract_user(bot, message, 2)

    if not user1 or not user2:
        await reply_and_delete(message, "I can't find one or both of the users.")
        return

    love_score = random.randint(0, 100)
    await message.edit_text(
        f"Love compatibility between {user1.mention} and {user2.mention}: **{love_score}%**"
    )