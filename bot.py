import discord
from discord.ext import commands

import time # for event logging 

f = open("TOKEN", "r")
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logged on at {time.ctime(time.time())} (UTC).')

'''
@bot.event
async def on_message(message):
    if message.author == bot.user: return
'''

@bot.command()
async def testme(ctx):
    await ctx.send("Beep boop, the rats begin to chew the sheets, boop boop...")
    return

bot.run(token)