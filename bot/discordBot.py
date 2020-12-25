import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def test(ctx):
    await ctx.send('its working')


client.run('add-channel-token-here')

