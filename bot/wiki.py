import wikipedia
import discord
from discord.ext import commands


def get_wiki_info(topic):
    return wikipedia.summary(topic, sentences=5)


class WikiCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(caseinsensitive=True, aliases=['wiki', 'wikipedia'])
    async def wikipedia_info(self, ctx):

        # asks for the wikipedia topic
        await ctx.send('What would you like to learn about?')
        wiki_topic = await self.client.wait_for('message',
                                                check=lambda message:
                                                message.author == ctx.author)

        embed = discord.Embed(
            description=get_wiki_info(wiki_topic.content),
            colour=discord.Colour.purple()
        )
        embed.set_author(name=wiki_topic.content,
                         icon_url=
                         'https://cdn.discordapp.com/avatars/775774976548405278'
                         '/14204b002e611c1dbca2418d012d955e.webp?size=128')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(WikiCog(client))

# self.client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')


