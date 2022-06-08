import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("OTgzOTU0MzU4NjI0NDgxMjgw.GpaQjs.S9EwxLo_01aoo3mQDN5LdIon9d6BjD6lfUVyX4")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run("OTgzOTU0MzU4NjI0NDgxMjgw.GpaQjs.S9EwxLo_01aoo3mQDN5LdIon9d6BjD6lfUVyX4")