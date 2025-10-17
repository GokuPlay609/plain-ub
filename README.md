# PLAIN UB: A Simple and Extensible Telegram User-Bot

![Header Image](assets/dark.png#gh-dark-mode-only)
![Header Image](assets/light.png#gh-light-mode-only)

Welcome to PLAIN UB, a simple yet powerful Telegram User-Bot designed for personalization and extensibility. This bot is built to be your personal assistant, and with its modular plugin architecture, you can easily add new features and commands to suit your needs.

## Table of Contents

- [How It Works](#how-it-works)
  - [Core Components](#core-components)
  - [Plugin Architecture](#plugin-architecture)
  - [Database System](#database-system)
- [Configuration](#configuration)
- [How to Create Your Own Commands](#how-to-create-your-own-commands)
  - [Basic Command](#basic-command)
  - [Command with Multiple Triggers](#command-with-multiple-triggers)
  - [Command with Database Access](#command-with-database-access)
  - [Conversational Command](#conversational-command)
- [List of Available Commands](#list-of-available-commands)

## How It Works

### Core Components

The userbot is built on top of the `ub_core` library, which provides the fundamental building blocks for the bot's functionality. This includes the main `BOT` object, message handling, and the `CustomDB` system.

### Plugin Architecture

The bot's functionality is extended through a modular plugin system. Each command or feature is contained within its own Python file, located in the `app/plugins/` directory. This makes it easy to add, remove, or modify commands without affecting the rest of the bot.

### Database System

The bot uses a simple key-value database system provided by `CustomDB`. This allows plugins to store and retrieve data in a persistent manner. Each key in the `CustomDB` object represents a "collection" of data, which is stored in a MongoDB database.

## Configuration

The userbot is configured using environment variables. These variables are defined in the `sample-config.env` file and can be set in your environment or in a `.env` file.

## How to Create Your Own Commands

Creating your own commands is simple and straightforward. Here are a few examples to get you started:

### Basic Command

```python
from app import BOT, Message

@BOT.add_cmd(cmd="test")
async def test_function(bot: BOT, message: Message):
    await message.reply("Testing....")
```

### Command with Multiple Triggers

You can assign multiple command triggers to a single function by passing a list to the `cmd` argument.

```python
from app import BOT, Message

@BOT.add_cmd(cmd=["cmd1", "cmd2"])
async def test_function(bot: BOT, message: Message):
    if message.cmd == "cmd1":
        await message.reply("cmd1 triggered function")
```

### Command with Database Access

You can use the `CustomDB` object to store and retrieve data in your plugins.

```python
from app import BOT, CustomDB, Message

TEST_COLLECTION = CustomDB["TEST_COLLECTION"]

@BOT.add_cmd(cmd="add_data")
async def test_function(bot: BOT, message: Message):
    # Find all data in the collection
    async for data in TEST_COLLECTION.find():
        print(data)

    # Add data to the collection
    await TEST_COLLECTION.add_data(data={"_id": "test", "data": "some_data"})

    # Delete data from the collection
    await TEST_COLLECTION.delete_data(id="test")
```

### Conversational Command

The bot also supports conversational commands, which allow you to interact with the user in a more dynamic way.

```python
from pyrogram import filters
from app import BOT, Convo, Message

@BOT.add_cmd(cmd="test")
async def test_function(bot: BOT, message: Message):
    async with Convo(
        client=bot,
        chat_id=message.chat.id,
        filters=filters.text,
        timeout=10
    ) as convo:
        await convo.get_response(timeout=10)
        await convo.send_message(text="abc", get_response=True, timeout=8)
```

## List of Available Commands

| Command | Description | Usage |
|---|---|---|
| `.flip` | Flips a coin. | `.flip` |
| `.flips` | Shows your coin flip history. | `.flips` |
| `.slap` | Slaps a user with a random object. | `.slap <reply/username>` |
| `.ship` | Ships two users together. | `.ship <reply/username> <reply/username>` |
| `.ships` | Shows your ship history. | `.ships` |
| `.roast` | Delivers a random roast to a user. | `.roast <reply/username>` |
| `.addroast` | Adds a roast to the database. | `.addroast <roast>` |
| `.compliment` | Delivers a random compliment to a user. | `.compliment <reply/username>` |
| `.addcompliment` | Adds a compliment to the database. | `.addcompliment <compliment>` |
| `.truth` | Provides a random truth question. | `.truth` |
| `.addtruth` | Adds a truth to the database. | `.addtruth <truth>` |
| `.dare` | Provides a random dare. | `.dare` |
| `.adddare` | Adds a dare to the database. | `.adddare <dare>` |
| `.hack` | Simulates hacking a user's account. | `.hack <reply/username>` |
| `.love` | Calculates love compatibility between two users. | `.love <username1> <username2>` |
| `.magic8ball` | Provides a Magic 8-Ball response to a question. | `.magic8ball <question>` |
| `.meme` | Fetches a random meme from Reddit. | `.meme` |
| `.ghost` | Sends a self-destructing message. | `.ghost <message>` |