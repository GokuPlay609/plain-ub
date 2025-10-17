import asyncio

from app import BOT, Message
from ub_core.utils import reply_and_delete


@BOT.add_cmd(cmd="ghost")
async def ghost(bot: BOT, message: Message):
    """
    CMD: GHOST
    INFO: Send a message that deletes itself after a few seconds.
    USAGE: .ghost <message>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to provide a message to ghost.")
        return

    await message.edit_text(message.text.split(maxsplit=1)[1])
    await asyncio.sleep(5)
    await message.delete()