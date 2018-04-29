from discord import *
from discord.ext import commands
from pyfont import pyfont as pf

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print('------')

@bot.command()
async def convert(text, fonttype):
    txt = pf.convert(text, fonttype)
    await bot.say(txt)

bot.run("NDM5NDU1MDY1MjQ2NDAwNTIy.DcTZ-w.AQPLSaVztrRhEffOH9rfYSxyevA")
