import discord
import os
import random
import time
import string

# Import the tokens from .env
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True
intents.presences = True

from discord.ext import commands

# client = discord.Client(command_prefix='!', intents=intents)

client = commands.Bot(command_prefix='.', intents=intents)

client.default_channel = "general"
client.channel_found = 0
client.cat_name = "cat"

# Testing by pinging the bot
@commands.command()
async def ping(ctx):
    print("ponging")
    await ctx.send("Pong!")
client.add_command(ping)

@commands.command()
async def defChannelSet(ctx, arg):
    arg.strip()
    for channel in ctx.guild.channels:
        channel_name = str(channel)
        channel_name.strip()
        print(channel_name)
        if str(arg) == channel_name:
            client.default_channel = str(arg)
            client.channel_found = 1

    if client.channel_found == 0:
        print("Channel set failure, " + str(arg) + " was not found in guild.")
        await ctx.send("*[CONFIG MODE]* Channel set failure, " + str(arg) + " was not found in guild.")
    else:
        print("Default channel is now " + str(arg))
        await ctx.send("*[CONFIG MODE]* Default channel is now " + str(arg))
        client.channel_found = 0

    print("client.default_channel = " + str(client.default_channel))

client.add_command(defChannelSet)

@commands.command()
async def setName(ctx, *arg):
    newName = ""
    for i in arg:
        newName = newName + " "+  i
    client.cat_name = newName[1:]
    await ctx.send("*[CONFIG MODE]* My name is now " + str(client.cat_name) + ".")
    # await client.user.edit(nick=client.cat_name)
    await ctx.guild.me.edit(nick=client.cat_name)

client.add_command(setName)

@commands.command()
async def printName(ctx):
    await ctx.send("*[CONFIG MODE]* My name is " + str(client.cat_name) + ".")

client.add_command(printName)


# Bot sign-on event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Determines which generic meow the bot will use
def mw_selector():
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

# Welcomes a user upon joining
@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")
    # channel = member.
    for channel in member.guild.channels:
        if str(channel) == client.default_channel:
            await channel.send(f"{member.mention} Meow meow meow meow meow! <3")

# @client.event
# async def catname(name):
#     await message.guild.get_member(self.user.id).edit(nick=name)

# Returns meow (or other related messages) for various key words
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    name = client.cat_name.lower()
    if name in message.content.lower():
        await message.channel.send(mw_selector())

    if 'meow' in message.content.lower():
        await message.channel.send(mw_selector())

    if 'mew' in message.content.lower():
        await message.channel.send(mw_selector())

    if 'mow' in message.content.lower():
        await message.channel.send(mw_selector())

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
        await message.channel.send(mw_selector())

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

    if 'woof' in message.content.lower():
        water_rand = random.randint(1,25)
        if water_rand == 24:
            await message.channel.send("woof")
            time.sleep(1)
            await message.channel.send("*coughing fit*")    
            time.sleep(1)
            await message.channel.send("MEOW!")
        else:
            await message.channel.send("*HISSSSSSSS*") 

    if 'bark' in message.content.lower():
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

    if 'good bot' in message.content.lower():
        await message.channel.send("*purrs*")

    if 'good cat' in message.content.lower():
        await message.channel.send("*purrs*")

    # Processes other commands as well
    await client.process_commands(message)

client.run(os.getenv('TOKEN'))
