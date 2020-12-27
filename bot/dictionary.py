import discord
from discord.ext import commands
from PyDictionary import PyDictionary

dictionary = PyDictionary()


def get_definition(word):
    word_meaning = PyDictionary(word)
    word_definitions = word_meaning.meaning(word)
    try:
        return word_definitions['Noun'][0]
    except KeyError:
        return word_definitions['Verb'][0]
    except:
        return word_definitions['Adjective'][0]


print(get_definition("water"))


class DictionaryCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(caseinsensitive=True, aliases=['define', 'definition'])
    async def word_definition(self, ctx):
        await ctx.send('What word would you like the definition for?')

        get_word = await self.client.wait_for('message',
                                              check=lambda message:
                                              message.author == ctx.author)

        embed = discord.Embed(
            description=get_definition(get_word.content),
            colour=discord.Colour.blue()
        )
        embed.set_author(name=get_word.content,
                         icon_url='https://cdn.discordapp.com/avatars/77577'
                                  '4976548405278/3a033aaeb4c112f7778fed109a'
                                  'f4c7a7.webp?size=128')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(DictionaryCog(client))
