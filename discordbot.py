import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

client = discord.Client ()
Client = commands.Bot (command_prefix = "+")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="+help | By MegaPig"))
    print("Bot Is Ready")

@Client.command()
async def help():
    await Client.say("L")
    
client.run(os.getenv('TOKEN'))
