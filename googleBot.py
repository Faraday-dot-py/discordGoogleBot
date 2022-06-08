import os

import discord
import wikipedia.exceptions
from dotenv import load_dotenv

import wikipedia as wk

from DISCORD_TOKEN import DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    print("Got response")

    if message.author == client.user:
        return

    if message.content == "!help":
        await message.channel.send("Use the command: !google [search term] to look up stuff.\nUse the command: !help to display this message")

    if message.content.find("!google") == 0:
        try:
            response = wk.summary(message.content[7:], sentences = 3)

            await message.channel.send(response)

        except wikipedia.exceptions.PageError:
            await message.channel.send("Was not able to find a page on {}".format(message.content[7:]))



client.run(DISCORD_TOKEN)