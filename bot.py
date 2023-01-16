import discord
import os
import random
import time

# Import the tokens from .env
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Bot sign-on event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Determines which generic meow the bot will use
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
        return "meow meow meow"

# Returns meow (or other related messages) for various key words
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'meow' in message.content.lower():
        await message.channel.send(meow_selector())

    if 'mew' in message.content.lower():
        await message.channel.send(meow_selector())

    if 'mow' in message.content.lower():
        await message.channel.send(meow_selector())

    if 'purr' in message.content.lower():
        await message.channel.send("*purrs*")

    if 'furries' in message.content.lower():
        await message.channel.send("*runs away*")

    if 'therapy animal' in message.content.lower():
        await message.channel.send("*runs away*")

    if 'therapy cat' in message.content.lower():
        await message.channel.send("*runs away*")

    if 'esa' in message.content.lower():
        await message.channel.send("*runs away*")

    if 'emotional support animal' in message.content.lower():
        await message.channel.send("*runs away*")

    if 'cat allergy' in message.content.lower():
        await message.channel.send("*scampers toward allergic individual*")

    if 'allergic to cats' in message.content.lower():
        await message.channel.send("*scampers toward allergic individual*")

    if 'allergic reaction' in message.content.lower():
        await message.channel.send("*scampers toward allergic individual*")
    
    if 'cat' in message.content.lower():
        await message.channel.send(meow_selector())

    if 'dog' in message.content.lower():
        water_rand = random.randint(1,25)
        if water_rand == 24:
            await message.channel.send("woof")
            time.sleep(1)
            await message.channel.send("*coughing fit*")    
            time.sleep(1)
            await message.channel.send("MEOW!")
        else:
            await message.channel.send("*HISSSSSSSS*") 

    if 'dawg' in message.content.lower():
        water_rand = random.randint(1,25)
        if water_rand == 24:
            await message.channel.send("woof")
            time.sleep(1)
            await message.channel.send("*coughing fit*")    
            time.sleep(1)
            await message.channel.send("MEOW!")
        else:
            await message.channel.send("*HISSSSSSSS*") 

    if 'k9' in message.content.lower():
        await message.channel.send("*HISSSSSSSS*") 

    if 'bird' in message.content.lower():
        await message.channel.send("*smacks lips*") 

    if 'fish' in message.content.lower():
        await message.channel.send("*smacks lips*")

    if 'purina' in message.content.lower():
        await message.channel.send("*smacks lips*") 

    if 'cat food' in message.content.lower():
        await message.channel.send("*smacks lips*")  

    if 'cat toy' in message.content.lower():
        await message.channel.send("MEOW! :D")

    if 'yarn' in message.content.lower():
        await message.channel.send("MEOW! :D")     

    if 'feather' in message.content.lower():
        await message.channel.send("MEOW! :D")

    if 'water' in message.content.lower():
        water_rand = random.randint(1,2)
        if water_rand == 1:
            await message.channel.send("*slurps*")    
        else:
            await message.channel.send("*HISSSSSSSS*") 

    if 'pet the cat' in message.content.lower():
        await message.channel.send("*purrs*")

    if 'pets cat' in message.content.lower():
        await message.channel.send("*purrs*")

    if 'pets' in message.content.lower():
        await message.channel.send("*purrs*")

    if 'pet' in message.content.lower():
        await message.channel.send("*purrs*")

client.run(os.getenv('TOKEN'))
