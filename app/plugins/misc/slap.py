import random

from app import BOT, CustomDB, Message
from ub_core.utils import extract_user, reply_and_delete

SLAPS = CustomDB["SLAPS"]


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

    slapper_stats = await SLAPS.find_one({"_id": slapper.id}) or {}
    slapped_stats = await SLAPS.find_one({"_id": slapped.id}) or {}

    await SLAPS.add_data(
        {
            "_id": slapper.id,
            "slapped_count": slapper_stats.get("slapped_count", 0) + 1,
        }
    )
    await SLAPS.add_data(
        {
            "_id": slapped.id,
            "slapped_by_count": slapped_stats.get("slapped_by_count", 0) + 1,
        }
    )