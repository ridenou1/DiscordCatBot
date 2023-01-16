import discord
import os
import random

# .env tokens
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def meow_selector():
    m1 = "meow"
    m2 = "mow"
    m3 = "mew"
    m4 = "meow meow"
    m5 = "*purr*"
    m6 = "meow?"
    selector = random.randint(1,10)
    if 1 <= selector <= 5:
        return m1
    elif selector == 6:
        return m2
    elif selector == 7:
        return m3
    elif selector == 8:
        return m4
    elif selector == 9:
        return m5
    elif selector == 10:
        return m6
    else:
        return m1

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_string = ""
    for i in message.content:
        message_string = message_string + i

    print(message_string)

    if 'meow' in message.content:
        await message.channel.send(meow_selector())

    if 'mew' in message.content:
        await message.channel.send(meow_selector())

    if 'mow' in message.content:
        await message.channel.send(meow_selector())

    if 'purr' in message.content:
        await message.channel.send("*purrs*")

    if 'furries' in message.content:
        await message.channel.send("*runs away*")

    if 'therapy animal' in message.content:
        await message.channel.send("*runs away*")

    if 'therapy cat' in message.content:
        await message.channel.send("*runs away*")

    if 'esa' in message.content:
        await message.channel.send("*runs away*")

    if 'emotional support animal' in message.content:
        await message.channel.send("*runs away*")

    if 'cat allergy' in message.content:
        await message.channel.send("*scampers toward allergic individual*")

    if 'allergic to cats' in message.content:
        await message.channel.send("*scampers toward allergic individual*")

    if 'allergic reaction' in message.content:
        await message.channel.send("*scampers toward allergic individual*")
    
    if 'cat' in message.content:
        await message.channel.send(meow_selector())

client.run(os.getenv('TOKEN'))
