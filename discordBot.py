from discord.ext import commands

from bot.quiz import QuizCog
from bot.wiki import WikiCog
from bot.reminder import ReminderCog
from bot.dictionary import DictionaryCog
from bot.translation import TranslationCog

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    client.add_cog(QuizCog(client))
    client.add_cog(WikiCog(client))
    client.add_cog(ReminderCog(client))
    client.add_cog(DictionaryCog(client))
    client.add_cog(TranslationCog(client))
    print('Bot is online')


client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')
