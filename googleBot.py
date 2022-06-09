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

    msg = message.content.lower()

    if msg == "!help":
        await message.channel.send("Use the command: !define [search term] to look up stuff.\nUse the command: !help to display this message")

    elif msg.find("jacob") != -1:
        await message.channel.send("Why are we talking about him again? Did someone want an example of an idiot?")

    elif msg == "!define ander":
        await message.channel.send("He got [bitches]")

    elif msg.find("shut up") != -1:
        await message.channel.send("No")

    elif msg.find("!define") == 0:

        word = msg[7:] if msg[7] != " " else msg[8:]

        definitionList = urbanDictClient.get_definition(word)

        try:

            definition = str(definitionList[0].definition)

            definition = definition.replace("[", "").replace("]", "")

            print(definition)

            await message.channel.send(definition)

        except IndexError:
            await message.channel.send("No definition was found on urban dictionary")

    elif msg == "!test!":
        await message.channel.send("Google Bot#1577 is currently connected")


dClient.run(DISCORD_TOKEN)
