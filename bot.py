import discord
from discord.ext import commands

import time # for event logging 

f = open("TOKEN", "r")
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} logged on at {time.ctime(time.time())} (UTC).')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content.startswith('&testme'):
        await message.channel.send('Beep Boop.. Ready to regulate.. bloop bloop')

client.run(token)