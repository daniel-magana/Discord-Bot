#import discord
import random

client = 1 #discord.Client()

bola_8=["Si",
        "Confirmo",
        "No",
        "A veces"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('bola 8'):
        await message.channel.send(random.choice(bola_8))

    elif message.content.startswith('better'):
        if message.content.endswith('top'):
            await message.channel.send('https://www.youtube.com/watch?v=RgRUFD_42aA')
        elif message.content.endswith('jg'):
            await message.channel.send('https://www.youtube.com/watch?v=Sr7ZUlsTwKc')
        elif message.content.endswith('mid'):
            await message.channel.send('https://www.youtube.com/watch?v=3aUa_xVjf-w')
        elif message.content.endswith('adc'):
            await message.channel.send('https://www.youtube.com/watch?v=coJJoFdIitM')
        elif message.content.endswith('supp'):
            await message.channel.send('https://www.youtube.com/watch?v=oqKURfz6fxg')

    elif message.content.startswith('holi'):
        await message.channel.send('Hola!')

client.run('somethingsomething')