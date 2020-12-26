import os
from discord.ext import commands

from bot.quiz import QuizCog
from bot.wiki import WikiCog

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    client.add_cog(QuizCog(client))
    client.add_check(WikiCog(client))
    print('Bot is online')

# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'bot.{extension}')
#
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'bot.{extension}')
#
#
# for filename in os.listdir
# (r'C:\Users\Mixna\PycharmProjects\discordBotProject\bot'):
#     if filename.endswith('.py'):
#         client.load_extension(f'{filename[:]}.py')


# @client.event
# async def on_ready():
#     print('Bot is online')


# @client.command()
# async def test(ctx):
#     await ctx.send('its working')


# @client.command(caseinsensitive=True, aliases=['addquestion', 'aq'])
# async def add_question(ctx):
#     await quiz.add_question(ctx)
#
#
# @client.command(caseinsensitive=True, aliases=['removequestion', 'rq'])
# async def remove_question(ctx):
#     await quiz.remove_question(ctx)
#
#
# @client.command(caseinsensitive=True, aliases=["viewall", "viewallquestions",
#                                                "viewquestionbank", "vqb"])
# async def view_question_bank(ctx):
#     await quiz.view_question_bank(ctx)
#
#
# @client.command(caseinsensitive=True, aliases=["askquestion", "askme", "ask",
#                                                'practice'])
# async def ask_question(ctx):
#     await quiz.ask_question(ctx, timeout=30)
#
#
# @client.command(caseinsensitive=True, aliases=["practiceall", 'askall',
#                                                "askallquestions"])
# async def ask_all_questions(ctx):
#     await ask_all_questions(ctx, timeout=30)
#
#
# @client.command(caseinsensitive=True, aliases=["testquestions", "testme"])
# async def test_questions(ctx):
#     await quiz.test_questions(ctx, num=5, timeout=30)
#
#
# @client.command(caseinsensitive=True, aliases=["testall", "testallquestions",
#                                                "testmeall"])
# async def test_all_questions(ctx):
#     await quiz.test_all_questions(ctx, timeout=30)

# def get_prefix(client, message):
#
#     prefixes = ['.']
#     if not message.guild:
#         return '?'
#     return commands.when_mentioned_or(*prefixes)(client, message)
#
#
# initial_extensions = ['cog.quiz']
#
#
# if __name__ == '__main__':
#     for extension in initial_extensions:
#         try:
#             client.load_extension(extension)
#         except Exception as e:
#             print(f'Failed to load extension {extension}', file=sys.stderr)
#             traceback.print_exc()

client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')
