import wikipedia

def get_wiki_info(topic):
    return wikipedia.summary(topic)

@client.command(caseinsensitive=True, aliases=['wiki', 'wikipedia'])
async def wikipedia_info(ctx):
    def check(m):
        return m.content is not None

    # asks for the wikipedia topic
    await ctx.send('What would you like to learn about?')
    wiki_topic = await client.wait_for('message', check=check)
    await ctx.send(get_wiki_info(wiki_topic))


