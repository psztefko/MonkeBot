from src.GenerateMessage import GenerateMessage
from discord.ext.commands import Bot
from random import randint
from pathlib import Path
from env import TOKEN
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

    messages = randint(2,3)
    readOutLoud = False

    if message.channel.name == 'communist-manifesto':
        if user_message.lower() == 'super':
            await message.channel.send(f'dzieki {username}')
        elif user_message.lower() == 'czytaj':
            readOutLoud = True
            messages = 1

        for i in range(messages):
            await message.channel.send(msg.get_sentences(), tts=readOutLoud)
            await message.channel.send(file=discord.File(Path(msg.get_image())))
            time.sleep(1.0)

client.run(TOKEN)


