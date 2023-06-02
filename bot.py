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

    class_selector_integer = random.randint(1, 10)
    class_role = 0

    if class_selector_integer in range(1, 4): # 30% chance to be poor
        class_role = user.server.get_role(1112870751415058532)

    elif class_selector_integer in range(4, 8): # 40% chance to be middle class
        class_role = user.server.get_role(1112870797690802226)
    else: # 30% chance to be upper class
        class_role = user.server.get_role(1112870829345218610)

    # print(f'DEBUG: @{user.id}\'s roles are: {user.roles}')
    await bot.add_roles(user, class_role)
    print(f'DEBUG: {user.id} was assigned {class_role.name} <{class_role.id}> at {time.ctime(time.time())} (UTC)')

    return

bot.run(token)