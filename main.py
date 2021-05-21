from src.GenerateMessage import GenerateMessage
from pathlib import Path
import discord

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

    if message.channel.name == 'dziad1':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')


        await message.channel.send(msg.get_sentences())

        await message.channel.send(file=discord.File(Path(msg.get_image())))

client.run('ODQ1MDI0MzI5NzU4MTQ2NTYx.YKa8PA.syIKVeLwLkMwGHp1QJqK5rgeoFM')


