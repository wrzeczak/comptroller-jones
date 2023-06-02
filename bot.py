import discord
from discord.ext import commands

import random

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

@bot.command()
async def roleup(ctx):
    user = ctx.message.author

    class_selector_integer = random.randint(1, 50)

    if class_selector_integer in range(1, 16): # 30% chance to be poor
        roles = user.roles # grab their roles
        print(f'DEBUG: @{user.id}\'s roles are: {user.roles}')

    if class_selector_integer 
    await ctx.send(f'@{user.id}, you\'re officially poor. Sorry!')
    return

bot.run(token)