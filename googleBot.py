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

    if message.author == dClient.user:
        return

    print("Got message")

    if message.content.lower() == "!help":
        await message.channel.send("Use the command: !define [search term] to look up stuff.\nUse the command: !help to display this message")

    elif message.content.lower().find("jacob") != -1:
        await message.channel.send("Why are we talking about him again? Did someone want an example of an idiot?")

    elif message.content.lower() == "!define ander":
        await message.channel.send("He got [bitches]")

    elif message.content.lower().find("shut up") != -1:
        await message.channel.send("No")

    elif message.content.lower().find("!define") == 0:

        word = message.content.lower()[7:] if message.content.lower()[7] != " " else message.content.lower()[8:]

        definitionList = urbanDictClient.get_definition(word)

        try:

            definition = definitionList[0].definition

            print(definition)

            await message.channel.send(definition)

        except IndexError:
            await message.channel.send("No definition was found on urban dictionary")

    elif message.content.lower() == "!test!":
        await message.channel.send("Google Bot#1577 is currently connected")


dClient.run(DISCORD_TOKEN)
