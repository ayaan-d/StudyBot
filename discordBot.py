from discord.ext import commands

from bot.quiz import QuizCog
from bot.wiki import WikiCog
from bot.dictionary import DictionaryCog

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    client.add_cog(QuizCog(client))
    client.add_cog(WikiCog(client))
    client.add_cog(DictionaryCog(client))
    print('Bot is online')


client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')
