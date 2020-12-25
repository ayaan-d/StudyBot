from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def test(ctx):
    await ctx.send('its working')

@client.command()
async def ask(ctx, question):
    response = [yes, no, maybe]

    if 
    await ctx.send('')



client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')

