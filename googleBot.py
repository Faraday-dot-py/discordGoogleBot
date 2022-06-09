import os

import discord
from dotenv import load_dotenv

from DISCORD_TOKEN import DISCORD_TOKEN

from udpy import UrbanClient

dClient = discord.Client()

urbanDictClient = UrbanClient()



@dClient.event
async def on_ready():
    print(f"{dClient.user} has connected to Discord!")

@dClient.event
async def on_message(message):
    print("Got message")

    if message.author == dClient.user:
        return

    if message.content == "!help":
        await message.channel.send("Use the command: !define [search term] to look up stuff.\nUse the command: !help to display this message")

    if message.content.find("jacob"):
        await message.channel.send("Why are we talking about him again? Did someone want an example of an idiot?")

    if message.content.find("!define") == 0:

        word = message.content[7:] if message.content[7] != " " else message.content[8:]

        definitionList = urbanDictClient.get_definition(word)

        try:

            definition = definitionList[0].definition

            print(definition)

            await message.channel.send(definition)

        except IndexError:
            await message.channel.send("No definition was found on urban dictionary")


dClient.run(DISCORD_TOKEN)