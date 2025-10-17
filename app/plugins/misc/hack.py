import asyncio
import random

from app import BOT, Message
from ub_core.utils import extract_user, reply_and_delete


@BOT.add_cmd(cmd="hack")
async def hack(bot: BOT, message: Message):
    """
    CMD: HACK
    INFO: A fun, harmless command that simulates hacking a user's account.
    USAGE: .hack <reply/username>
    """
    user, reason = await extract_user(bot, message)
    if not user:
        await reply_and_delete(message, f"I can't find that user.")
        return

    hacked_user = user.first_name
    hacked_user_id = user.id
    chat_id = message.chat.id
    progress = 0
    hacking_message = await bot.send_message(
        chat_id, f"Hacking {hacked_user}'s account..."
    )

    while progress < 100:
        progress += random.randint(1, 5)
        if progress > 100:
            progress = 100
        await hacking_message.edit_text(
            f"Hacking {hacked_user}'s account... {progress}%"
        )
        await asyncio.sleep(0.1)

    await hacking_message.edit_text(
        f"Successfully hacked {hacked_user}'s account!\n"
        f"Their user ID is: `{hacked_user_id}`"
    )