import discord
from discord.ext import commands

import random

import time # for event logging 

f = open("TOKEN", "r")
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents)

class_roles = [ 1112870751415058532, 1112870797690802226, 1112870829345218610 ] # low, middle, high
class_weights = [ .3, .4, .3 ]

race_roles = [ 1114976043766403122, 1114976195528892597, 1114976121642045450 ] # purple, pink, green
race_weight = [ .45, .15, .4 ]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

    class_role = ctx.message.guild.get_role(random.choices(class_roles, weights=class_weights, k=1)[0])

    race_role = ctx.message.guild.get_role(random.choices(race_roles, weights=race_weight, k=1)[0])

    # print(f'DEBUG: @{user.id}\'s roles are: {user.roles}')
    await user.add_roles(class_role, race_role)
    print(f'DEBUG: {user.id} was assigned {class_role.name}, {race_role.name} <{class_role.id}>, <{race_role.id}> at {time.ctime(time.time())} (UTC)')

    await ctx.send(f"Assigned class {class_role.name} and race {race_role.name}... many such cases...")
    return

@bot.command()
async def weights(ctx):
    output = discord.Embed(colour=None, title="Race/Class Weights")

    for i in range(0, len(race_roles)):
        output.add_field(title=ctx.message.guild.get_role(race_roles[i]).name, value=f'{race_weight[i] * 100}%')

    for i in range(0, len(race_roles)):
        output.add_field(title=ctx.message.guild.get_role(class_roles[i]).name, value=f'{class_weights[i] * 100}%')

    await ctx.send(output)


bot.run(token)