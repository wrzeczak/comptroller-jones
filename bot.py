import discord
from discord.ext import commands

f = open("TOKEN", "r")
token = f.read()

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot Ready!")

bot.run(token)

# test comment to test github + vscode functionality