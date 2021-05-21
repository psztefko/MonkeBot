from src.GenerateMessage import GenerateMessage
from discord.ext.commands import Bot
from random import randint
from pathlib import Path
import discord
import time

client = discord.Client()

msg = GenerateMessage()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    sentences = randint(2,3)
    readOutLoud = False

    if message.channel.name == 'test':
        if user_message.lower() == 'super':
            await message.channel.send(f'dzieki {username}')
        elif user_message.lower() == 'czytaj':
            readOutLoud = True
            sentences = 1

        for i in range(sentences):
            await message.channel.send(msg.get_sentences(), tts=readOutLoud)
            await message.channel.send(file=discord.File(Path(msg.get_image())))
            time.sleep(1.0)

client.run('ODQ1MDI0MzI5NzU4MTQ2NTYx.YKa8PA.syIKVeLwLkMwGHp1QJqK5rgeoFM')


