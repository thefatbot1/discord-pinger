import colorama
from colorama import Fore, Back, Style
import discord
from discord.ext import commands

print(Fore.RED +'whats ur bot token?')  #right click to paste ur bot token in input
token = input()

print(Fore.LIGHTGREEN_EX + f'token set as {token}')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx):
    while True:
        await ctx.send('@everyone')

print('')
print('type in $ping in discord chat to spam ping')
print('')

bot.run(token)