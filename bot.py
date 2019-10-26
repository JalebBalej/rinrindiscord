import discord
import random
import os
from discord.ext import commands

BotOwnerID = 171409282439446528

f = open("token", "r")
TOKEN = f.read()
f.close()
client = commands.Bot(command_prefix='rr.')
client.remove_command('help')

@client.event
async def on_connect():
    await client.change_presence(activity=discord.Game("CONNECTED!"))
    print('Rin Rin has established a connection to Discord!')

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
async def on_command_error(ctx, error):
    log = open("log", "w+")
    log.write(f"Error: {error}")
    log.close()
    if isinstance(error, commands.CommandNotFound):
        member = ctx.message.author.id
        if os.path.exists(f"memlangs\{member}"):
            languageCheck = open(f"memlangs\{member}", "r")
            memlanguage = languageCheck.read()
            if memlanguage == "en":
                languageCheck.close()
                await ctx.send("Command not found! Check to see if it was a typo!")
            else:
                languageCheck.close()
                await ctx.send("コマンドが見つかりません！タイプミスかどうかを確認してください！")
        else:
            languageCreate = open(f"memlangs\{member}", "w+")
            languageCreate.write("en")
            languageCreate.close()
            await ctx.send("Command not found! Check to see if it was a typo!")
    else:
        member = ctx.message.author.id
        if os.path.exists(f"memlangs\{member}"):
            languageCheck = open(f"memlangs\{member}", "r")
            memlanguage = languageCheck.read()
            if memlanguage == "en":
                await ctx.send("Whoops! I ran into an error! Nobu-kun check my log please!")
            else:
                await ctx.send("おっと！エラーが発生しました！ノブくんのログをチェックしてください！")
        else:
            languageCreate = open(f"memlangs\{member}", "w+")
            languageCreate.write("en")
            languageCreate.close()
            await ctx.send("Whoops! I ran into an error! Nobu-kun check my log please!")



@client.command(aliases=['?','h'])
async def help(ctx):
    embed = discord.Embed(title="Rin Rin ❤ Help", description="version 10.26.19.7.5a", color=2367979)
    embed.add_field(name="rr.help", value="Shows this message", inline=False)
    embed.add_field(name="rr.rn (startnumber)(endnumber)", value="Gets a random number from start to end.", inline=False)
    embed.add_field(name="rr.match (name) (partner)", value="Calculates compatibility with name and partner.", inline=False)
    embed.add_field(name="rr.ping", value="Shows my ping!", inline=False)
    embed.add_field(name="rr.py", value="Shows current discord.py version I'm running.")
    embed.add_field(name="rr.info", value="Shows bot info!", inline=False)
    embed.add_field(name="rr.hi", value="Say hi!", inline=False)
    embed.add_field(name="rr.iloveyou", value="Say I love you, and get rejected.", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Rin Rin ❤ Info", description="About me!", color=8993300)
    embed.add_field(name="Bot Author:", value="Nobuyaki#4974", inline=False)
    embed.add_field(name="Bot Version:",value="10.25.19.11.2p", inline=False)
    embed.add_field(name="Github Link:", value="https://github.com/liberation4you/rinrindiscord", inline=False)
    embed.set_footer(text="Rin Rin ❤",icon_url="https://avatars1.githubusercontent.com/u/53136821?s=400&u=7877010f24ed4d436db5f1c6aa559fde428dcb31&v=4")
    await ctx.send(embed=embed)


@client.command()
async def hi(ctx):
    await ctx.send("hiiii")

@client.command()
async def lang(ctx, language: str = None):
    memberID = ctx.message.author.id
    if language == "en":
        file = open(f"memlangs\{memberID}", "w+")
        file.write("en")
        await ctx.send(f"Changed your language to **English**!")
        file.close()
    else:
        if language == "jp":
            file = open(f"memlangs\{memberID}", "w+")
            file.write("jp")
            await ctx.send(f"Changed your language to **Japanese**!")
            file.close()
        else:
            if language is None:
                if os.path.exists(f"memlangs\{memberID}"):
                    file = open(f"memlangs\{memberID}", "r")
                    currentlang = file.read()
                    await ctx.send(f"Your current language is {currentlang}!")
                    file.close()
                else:
                    file = open(f"memlangs\{memberID}", "w+")
                    print(f"Rin Rin TempLog> {memberID} doesn't have lang file! Creating one.")
                    await ctx.send(f"You don't have a lang file so I made you one! Default language is **English**.\nType rr.lang again to see language.")
                    file.write("en")
                    file.close()
            else:
                await ctx.send("Incorrect language! Type 'en' for English or 'jp' for Japanese.")



@client.command()
async def iloveyou(ctx):
    member = ctx.message.author.id
    if member == BotOwnerID:
        await ctx.send("i love you tooooo :heart: :heart:")
    else:
        await ctx.send("well, i don't love you")

@client.command()
async def py(ctx):
    await ctx.send(f"I'm currently using discord.py version {discord.__version__}! :slight_smile:")

@client.command()
async def ping(ctx):
    await ctx.send(f'Bot latency is {round(client.latency * 1000)}ms!')

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
