from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is online')


@client.command()
async def test(ctx):
    await ctx.send('its working')


@client.command(aliases=['addquestion'])
async def add_question(ctx, question=None):

    def check(m):
        return m.content is not None

    if question is None:
        await ctx.send('Please input the question you would like to add to the '
                       'question bank')
        question = await client.wait_for('message', check=check)
    await ctx.send('Please input the correct answer for the previously'
                   ' inputted question')
    answer = await client.wait_for('message', check=check)
    # add question to csv
    # add answer to csv
    # add channel to csv
    await ctx.send(f"The question, '{question.content}' and its answer, '{answer.content}' was "
                   f"successfully added to the question bank")


@client.command()
async def remove_question(ctx):
    # print all the questions in the question bank with numbers
    # remove accordingly
    question = ""
    answer = ""
    await ctx.send(f"{question} and its answer, '{answer}'"
                   f"was successfully removed from the question bank")


client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')

