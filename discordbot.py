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

   
@client.event
async def on_message(message):
    if message.content.startswith('+info'):
        await client.send_message(message.channel, """Hello! My name is MegaBot!
I have 3 types of commands:
**Information Commands**
**General Commands**
**Staff Commands**
For see all the commands type: __+help__""")

    if message.content.startswith('+creator'):
        await client.send_message(message.channel, """**My Creator Is MegaPig#1576!**""")
        
    if message.content.startswith('+invite'):
        await client.send_message(message.channel, """https://discordapp.com/api/oauth2/authorize?client_id=459490391146627073&permissions=8&scope=bot
__You Can Invite Me When Ever You Want!__
You Can Help If You Say Bugs To My Creator- **MegaPig#1576**""")

    if message.content.startswith('+help'):
        embed = discord.Embed(title="Command List", description="""
__**Information Commands**__

**+info** - Small Information Of The Bot.
**+invite** - The Bot Invite Link.
**+creator** - The Bot Creator.

__**General Commands**__

**+avatar @tag** - The avatar of the member.
**+servericon** - the picture of the server.
**+servers** - how many servers the bot in.
**+question (שאלת כן ולא)** - The Bot answear to you.

__**Staff Commands**__

**+warn** @TAG- warn member (move members permission)
**+mute** @TAG- mute member (mute members permission)
**+clear (2-100)** - clear messages (manage_messages permission)
**+kick** @TAG - kick member (kick members permission)
**+ban** @TAG - ban member (ban members permission)
""", color=0xe88af4)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('תצעק'):
        await client.send_message(message.channel, "האהאהאההאהאהאהאהאהאהאהאאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאאהאההאהההאהאהאהאהאהאאהאהאהאהאהאהאאהאאאהאאאהאהאהאאהאההאהאאההאהאאהאהאהאהאאהאהאהאהאהאהאהאאהאהאהאהאהאאהאהאהאהאהאהאאהאהאהאהאאהאהאהאהאאהאהאהאהאהאהאהאהאההאההאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאהאהאאהאהאהאהאההאאהאהאהאהאהאהאהאהאהאהאאהאהאהאהאאההאאהאהאהאהאהאהאהאהאהאאאהאהאהאהאהאהאהאהאהאהה")
    await Client.process_commands(message)
        
@Client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)
        
        
client.run(os.getenv('TOKEN'))
