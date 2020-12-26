from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is online')


@client.command()
async def test(ctx):
    await ctx.send('its working')


# noinspection SpellCheckingInspection
@client.command(aliases=["addquestion"])
async def add_question(ctx, question):
    answer = await client.wait_for('Please input the correct answer for '
                                   'the inputted question')
    # add question to csv
    # add answer to csv
    # add channel to csv
    await ctx.send(f"{question} and its answer, '{answer}' was successfully "
                   f"added to the question bank")


client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')

