import random

from app import BOT, Message
from app.core.db.models import Slaps
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="slap")
async def slap(bot: BOT, message: Message):
    """
    CMD: SLAP
    INFO: Slap a user with a random funny object.
    USAGE: .slap <reply/username>
    """
    user, _ = await extract_user(bot, message)
    if not user:
        await reply_and_delete(message, f"I can't find that user.")
        return

    slapper = message.from_user
    slapped = user
    slap_objects = [
        "a large trout",
        "a wet noodle",
        "a rubber chicken",
        "a rusty spoon",
        "a giant inflatable hammer",
    ]
    slap_object = random.choice(slap_objects)

    await message.edit_text(
        f"{slapper.mention} slaps {slapped.mention} with {slap_object}!"
    )

    slapper_stats, _ = await Slaps.get_or_create(user_id=slapper.id)
    slapper_stats.slapped_count += 1
    await slapper_stats.save()

    slapped_stats, _ = await Slaps.get_or_create(user_id=slapped.id)
    slapped_stats.slapped_by_count += 1
    await slapped_stats.save()