#imports
import discord
from discord.ext import commands

#set up our bot name, command prefix, and intents
tobey = commands.Bot(command_prefix="!", intents=discord.Intents.all())

token = open("token.txt", "r").read()

#commands
@tobey.command()
async def ping(ctx):
    bot_latency = round(tobey.latency*1000)
    await ctx.send(f"pong! {bot_latency} ms.")

#run your bot
@tobey.event 
async def on_ready():
    print("tobey has entered the server's realm.")

#final run - do not put anything under here!!
tobey.run(token)