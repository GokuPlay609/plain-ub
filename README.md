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
  - [Admin Commands](#admin-commands)
  - [AI Commands](#ai-commands)
  - [File Commands](#file-commands)
  - [Misc Commands](#misc-commands)
  - [Sudo Commands](#sudo-commands)
  - [Telegram Tools](#telegram-tools)

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

### Admin Commands

| Command | Description | Usage |
|---|---|---|
| `.ban` | Bans a user from the chat. | `.ban <reply/username> [reason]` |
| `.unban` | Unbans a user from the chat. | `.unban <reply/username> [reason]` |
| `.unmute` | Unmutes a user in the chat. | `.unmute <reply/username> [reason]` |
| `.addf` | Adds a fed chat to the database. | `.addf [name]` |
| `.delf` | Deletes a fed from the database. | `.delf [id]` or `.delf -all` |
| `.listf` | Lists the connected feds. | `.listf` or `.listf -id` |
| `.fban` | Initiates a fed-ban. | `.fban <uid/@/reply> [reason]` |
| `.fbanp` | Initiates a fed-ban with proof. | `.fbanp <uid/@/reply> [reason]` |
| `.unfban` | Initiates a fed-unban. | `.unfban <uid/@/reply> [reason]` |
| `.kick` | Kicks a user from the chat. | `.kick <reply/username> [reason]` |
| `.kick_im` | Kicks inactive members. | `.kick_im` |
| `.mute` | Mutes a user in the chat. | `.mute <reply/username> [reason]` |
| `.promote` | Promotes a user to admin. | `.promote [-anon/-full] <uid/@/reply> [title]` |
| `.demote` | Demotes a user from admin. | `.demote <uid/@/reply>` |
| `.demote_all` | Demotes all admins in the chat. | `.demote_all` |
| `.zombies` | Cleans deleted accounts from the chat. | `.zombies` |

### AI Commands

| Command | Description | Usage |
|---|---|---|
| `.gpt` | Asks a question to ChatGPT. | `.gpt <question>` or `.gpt <reply>` |
| `.igen` | Generates images using DALL-E. | `.igen <prompt>` |
| `.aic` | Starts a conversation with Gemini AI. | `.aic <prompt>` |
| `.lh` | Loads a conversation with Gemini AI from history. | `.lh <question> <reply to history file>` |
| `.ai` | Asks a question to Gemini AI. | `.ai <prompt>` |

### File Commands

| Command | Description | Usage |
|---|---|---|
| `.download` | Downloads files or Telegram media. | `.download <url/reply>` or `.download -f <filename> <url/reply>` |
| `.gsetup` | Sets up Google Drive credentials. | `.gsetup <reply to credentials.json>` |
| `.agcreds` | Adds pre-generated Google Drive credentials. | `.agcreds <data>` |
| `.rgcreds` | Removes Google Drive credentials. | `.rgcreds` |
| `.gls` | Lists files and folders from Google Drive. | `.gls [-f/-d] [-l <limit>] [search_param]` |
| `.gup` | Uploads a file to Google Drive. | `.gup [-id <folder_id>] <url/reply>` |
| `.l` | Leeches a URL to Telegram. | `.l <-p/-a/-v/-g/-d> [-s] <link/file_id>` |
| `.rename` | Renames and uploads a file. | `.rename <url/reply> <new_filename>` |
| `.spoiler` | Marks a media file as a spoiler. | `.spoiler <reply to photo/video>` |
| `.upload` | Uploads a file to Telegram. | `.upload [-d/-s] <url/path/cmd>` or `.upload -bulk [-r] <path>` |

### Misc Commands

| Command | Description | Usage |
|---|---|---|
| `.alive` | Shows bot information. | `.alive` |
| `.extupdate` | Updates external modules. | `.extupdate` |
| `.ln` | Checks LastFM status. | `.ln` |
| `.sn` | Checks Spotipie status. | `.sn` |
| `.song` | Downloads a song from YouTube. | `.song <song_name/url>` |
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

### Sudo Commands

| Command | Description | Usage |
|---|---|---|
| `.addscmd` | Adds sudo commands. | `.addscmd <cmd_name>` or `.addscmd -all` |
| `.delscmd` | Removes sudo commands. | `.delscmd <cmd_name>` or `.delscmd -all` |
| `.vscmd` | Views sudo commands. | `.vscmd` |
| `.disable_su` | Disables your superuser access. | `.disable_su` |
| `.enable_su` | Enables your superuser access. | `.enable_su` |
| `.sudo` | Enables or disables sudo. | `.sudo` or `.sudo -c` |
| `.addsudo` | Adds a sudo user. | `.addsudo [-temp/-su] <uid/@/reply>` |
| `.delsudo` | Removes a sudo user. | `.delsudo [-temp/-su] <uid/@/reply>` |
| `.vsudo` | Views sudo users. | `.vsudo` or `.vsudo -id` |

### Telegram Tools

| Command | Description | Usage |
|---|---|---|
| `.ids` | Gets the IDs of a chat or user. | `.ids` or `.ids <username>` or `.ids <reply>` |
| `.join` | Joins a chat. | `.join <chat_username>` |
| `.leave` | Leaves a chat. | `.leave` or `.leave <chat_username>` |
| `.click` | Clicks a button in a replied message. | `.click <button_text/index>` |
| `.del` | Deletes a message. | `.del` or `.del -r <message_link>` |
| `.del_uh` | Deletes a user's history in a chat. | `.del_uh <reply>` |
| `.purge` | Purges messages in a chat. | `.purge <reply>` |
| `.gm` | Gets a message's JSON or attribute. | `.gm <message_link> [attribute]` |
| `.kang` | Kangs a sticker. | `.kang` or `.kang -f` |
| `.ping` | Checks the bot's ping. | `.ping` |
| `.taglogger` | Enables or disables the tag logger. | `.taglogger` or `.taglogger -c` |
| `.pmlogger` | Enables or disables the PM logger. | `.pmlogger` or `.pmlogger -c` |
| `.pmguard` | Enables or disables the PM guard. | `.pmguard` or `.pmguard -c` |
| `.a` or `.allow` | Allows a user to PM you. | `.a` or `.allow` or `.a <uid/@/reply>` |
| `.nopm` | Disallows a user to PM you. | `.nopm` or `.nopm <uid/@/reply>` |
| `.reply` | Replies to a message. | `.reply <text>` or `.reply -r <message_link> <text>` |
| `.resp` | Responds to a logged message. | `.resp <chat_id/reply> <text>` |
| `.ghost` | Sends a self-destructing message. | `.ghost <message>` |
