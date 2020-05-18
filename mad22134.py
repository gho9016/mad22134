import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!?')

@bot.event
async def on_ready():
    print('등장!')

@bot.command()
async def 핑(ctx):
    await ctx.send('퐁 {0}초'.format(bot.latency))

bat.run('NzExOTIxOTIxOTg1NjA5NzM5.XsKE3w.Qhr-2HzvWQmki2F7ICcNr3Wz5N8')
