import random
import asyncpraw
from app import BOT, Message, extra_config
from ub_core.utils import reply_and_delete


@BOT.add_cmd(cmd="meme")
async def meme(bot: BOT, message: Message):
    """
    CMD: MEME
    INFO: Get a random meme from Reddit.
    USAGE: .meme
    """
    if not extra_config.REDDIT_CLIENT_ID or not extra_config.REDDIT_CLIENT_SECRET or not extra_config.REDDIT_USER_AGENT:
        await reply_and_delete(message, "Reddit API credentials are not configured. Please set them in `extra_config.py`.")
        return

    reddit = asyncpraw.Reddit(
        client_id=extra_config.REDDIT_CLIENT_ID,
        client_secret=extra_config.REDDIT_CLIENT_SECRET,
        user_agent=extra_config.REDDIT_USER_AGENT,
    )
    try:
        subreddit = await reddit.subreddit("memes")
        hot_memes = [meme async for meme in subreddit.hot(limit=100)]
        random_meme = random.choice(hot_memes)
        await bot.send_photo(message.chat.id, random_meme.url)
    except Exception as e:
        await reply_and_delete(message, f"Could not fetch a meme at this time. Error: {e}")
    finally:
        await reddit.close()