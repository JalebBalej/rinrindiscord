import discord
import random
import sqlite3
from sqlite3 import Error
from discord.ext import commands

database = r"G:\stuff\python shit\rin rin bot\rinrinbotsqlite.db"
BotOwnerID = '171409282439446528'

f = open("token", "r")
TOKEN = f.read()
f.close()
client = commands.Bot(command_prefix='rr.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("こんいちわみなさん！"))
    print('Rin Rin is ready and running discord.py version ' + discord.__version__)

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server!')

@client.event
async def on_message(message):
    if message.content.startswith("hi rin"):
            channel = message.channel
            await channel.send("hiii")
    if message.content.startswith("i love you rin"):
        if message.author.id == BotOwnerID:
            channel = message.channel
            await channel.send("i love you tooooo")
        else:
            channel = message.channel
            await channel.send("well that sucks because i don't love you")


#@client.command()
#async def testlocalization(ctx):
#    def create_connection(database):
#        conn = sqlite3.connect(database)

#Work In Progress Command (I don't have a clue how to do this), please help, I want to make a localization system
#This is the command to switch the language in the server, but I don't know how to do anything at all here
#@client.command()
#async def lang(ctx, language: str):
#    if language == ['english','testjapanese']:

@client.command()
async def py(ctx):
    await ctx.send(f"I'm currently using discord.py version {discord.__version__}! :slight_smile:")

@client.command()
async def ping(ctx):
    await ctx.send(f'Bot latency is {round(client.latency * 1000)}ms!')

@client.command(aliases=['?','h'])
async def help(ctx):
    await ctx.send(f"Rin Rin ❤ Help version 10.23.19.2.0p\nrr.help -- Shows this message\nrr.rn (start number) (end number) -- Sends random number from start to end.\nrr.match (name1) (name2) -- Compatibilty with name1 and name2.\nrr.ping -- Shows my ping.\nrr.py -- Shows current discord.py version I'm using.")

@client.command()
async def rn(ctx, number1: int, number2: int):
    randnum = random.randint(number1, number2)
    await ctx.send(f"Your random number is **{randnum}**.")

@rn.error
async def rn_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You need to enter two numbers when entering that command!")

@client.command()
async def match(ctx, name: str, partner: str):
    matchchance = random.randint(1, 100)
    if matchchance == 100:
        await ctx.send(f"{name} :two_hearts: {partner}\nCompatibilty is {matchchance}%!\n**Congratulations on getting 100% compatibilty {name} and {partner}!**")
    else:
        if matchchance < 50:
            await ctx.send(f"{name} :heart: {partner}\nCompatibilty: {matchchance}%\nBetter luck next time!")
        else:
            await ctx.send(f"{name} :heart: {partner}\nCompatibilty: {matchchance}%")

@match.error
async def match_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Don't forget to specify two names!")

client.run(TOKEN)
