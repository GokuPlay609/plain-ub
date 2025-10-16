import random

from app import BOT, Message
from ub_core.utils import reply_and_delete


@BOT.add_cmd(cmd="magic8ball")
async def magic8ball(bot: BOT, message: Message):
    """
    CMD: MAGIC8BALL
    INFO: Ask the Magic 8-Ball a question.
    USAGE: .magic8ball <question>
    """
    if not message.text.split(maxsplit=1)[1:]:
        await reply_and_delete(message, "You need to ask a question.")
        return

    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    answer = random.choice(answers)
    await message.edit_text(f"**Magic 8-Ball says:** {answer}")