# bot.py
import os
import random
import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
bot = Bot('.')

client = commands.Bot(command_prefix = '.')

import dotenv
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Yo Fucker {member.name}, This my Discord Server my name is fuckin johnny and respect dat!'
    )

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    
bot = commands.Bot(command_prefix='.')

@bot.command()
async def test(ctx):
    await ctx.send(arg)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'Oh baby I love it when you talk to me like that *gets boner*',
        'PLEASE GET BACK TOGETHER WITH ME',
        (
            'Fuck You. I WANT A DIVORCE, '
            'YOU ABSOULUTE PEICE OF GARBAGE GET OUT OF HERE YOU WASTE OF AIR!'
        ),
    ]

    if message.content == '.randommarry':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        
client.run(TOKEN)