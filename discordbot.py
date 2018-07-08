import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import os

client = discord.Client ()
Client = commands.Bot (command_prefix = "+")
Client.remove_command("help")

@client.event
async def on_ready():
    print("MegaBot is now Online!")

@Client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant mute this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.kick_members or ctx.message.author.id == '194151340090327041':
       await Client.kick(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Kicked!", description="**{0}** was kick by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant kick this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def warn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.move_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Warn')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Warned!", description="**{0}** was warned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant warn this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
       await Client.ban(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Baned!", description="**{0}** was ban by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant ban this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def clear(ctx, amount=100):
    if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == '194151340090327041':
       channel = ctx.message.channel
       messages = []
       async for message in Client.logs_from(channel, (amount)):
            messages.append(message)
       await Client.delete_messages(messages)
       await Client.say("**The Messages delete!**")
    else:
        embed=discord.Embed(title="You cant Do This Command!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await Client.change_presence(game=discord.Game(name=game))
        except:
            await Client.say("Failed to change game")
        else:
            await Client.say("Successfuly changed game to {}".format(game))
    else:
        await Client.send_cmd_help(ctx)

@Client.command()
async def servers():
  	"""Bot Guild Count"""
  	await Client.say("**I'm in {} servers!**".format(len(Client.servers)))

@Client.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await Client.reply("{}".format(ctx.message.server.icon_url))

@Client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await Client.reply("{}".format(member.avatar_url))

@Client.command(pass_context=True)
async def question(ctx):

	possible_responses = ["לא", "כן", "אני לא בטוח, תשאל שוב אולי אני יחליט"]

	current_response = random.choice(possible_responses)

	await Client.say(current_response)

@Client.command(pass_context = True)
async def instantwarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.move_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='instantwarn')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User instantWarned!", description="**{0}** was instantwarned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant instantwarn this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)


@Client.command(pass_context = True)
async def removewarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.send_messages or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='instantwarn')
        await Client.remove_roles(member, role)
	
    
client.run(os.getenv('TOKEN'))
