#!/bin/python3


# bot.py
import os

import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.lower().startswith('are you there'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

client.run(TOKEN)
