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

    brooklyn_99_quotes = [
            'The universe is big. It’s vast and complicated and ridiculous. And sometimes, very rarely, impossible things just happen and we call them miracles.',
            'Do what I do. Hold tight and pretend it’s a plan!',
            'Rule 1: The Doctor lies.',
            'I am and always will be the optimist. The hoper of far-flung hopes and the dreamer of improbable dreams.',
            'The way I see it, every life is a pile of good things and bad things. The good things don’t always soften the bad things, but vice versa, the bad things don’t always spoil the good things and make them unimportant.',
            'Everybody knows that everybody dies. But not every day. Not today. Some days are special. Some days are so, so blessed. Some days, nobody dies at all. Now and then, every once in a very long while, every day in a million days, when the wind stands fair and the Doctor comes to call, everybody lives.',
            'You don’t just give up. You don’t just let things happen. You make a stand! You say no! You have the guts to do what’s right, even when everyone else just runs away.',
            'Some people live more in twenty years than others do in eighty. It’s not the time that matters, it’s the person.',
            'You know, the very powerful and the very stupid have one thing in common: they don’t alter their views to fit the facts; they alter the facts to fit their views.',
            'Never cruel or cowardly. Never give up, never give in.',
            'Rest is for the weary, sleep is for the dead.',
            'Hermits United. We meet up every 10 years, swap stories about caves. It’s good fun… for a hermit.',
            'There’s a lot of things you need to get across this universe. Warp drive… wormhole refractors… You know the thing you need most of all? You need a hand to hold.',
            'People assume that time is a strict progression of cause to effect, but actually from a non-linear, non-subjective viewpoint – it’s more like a big ball of wibbly wobbly… time-y wimey… stuff.',
            'Amy Pond, there’s something you’d better understand about me ‘cause it’s important, and one day your life may depend on it: I am definitely a mad man with a box!',
            'Don’t blink. Don’t even blink. Blink and you’re dead. Don’t turn your back. Don’t look away. And don’t blink.',
            'I’ll be a story in your head. That’s okay. We’re all stories in the end. Just make it a good one, eh? ‘Cause it was, you know. It was the best. The daft old man who stole a magic box and ran away. Did I ever tell you that I stole it? Well I borrowed it. I was always going to take it back.',
            'One may tolerate a world of demons for the sake of an angel.',
            'Rose, before I go, I just want to tell you: you were fantastic. Absolutely fantastic. And you know what? So was I.',
            'Good men don’t need rules.'
            ]

    if message.content.lower() == 'doctor':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if 'happy birthday' in message.content.lower():
        for i in range(10):
            await message.channel.send('Happy Birthday! 🎈🎉')


client.run(TOKEN)
