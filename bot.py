import random

import discord
from discord.ext import commands

from datetime import datetime

import sqlite3 as sql
from sqlite3 import Error

from cogs.locale import *



BotVersion = "v 10.31.19.17.4"
BotOwnerID = 171409282439446528

conn = sql.connect("Database.db")
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS users (
                    u_id INTEGER PRIMARY KEY,
                    name TEXT,
                    id INTEGER,
                    lang TEXT DEFAULT 'en'
                ); """)
cur.execute(""" CREATE TABLE IF NOT EXISTS logs (
                    u_id INTEGER PRIMARY KEY,
                    name TEXT,
                    id INTEGER,
                    cause TEXT,
                    time TEXT,
                    unix_time INTEGER
                ); """)
cur.close()

all_languages = {
    "english": "en",
    "russian": "ru",
    "lithuanian": "lt"
}

f = open("token", "r")
TOKEN = f.read()
f.close()
client = commands.Bot(command_prefix='rr.')
client.remove_command('help')

@client.event
async def on_connect():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    await client.change_presence(activity=discord.Game("CONNECTED!"))
    print(f'Time: {time} | Rin Rin has established a connection to Discord!')

@client.event
async def on_ready():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    await client.change_presence(activity=discord.Game("こんいちわみなさん！"))
    print(f'Time: {time} | Rin Rin is ready and running discord.py version ' + discord.__version__)

@client.event
async def on_member_join(member):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(f'Time: {time} | {member} has joined a server!')

@client.event
async def on_member_remove(member):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(f'Time: {time} | {member} has left a server!')

@client.event
async def on_command_error(ctx, error):
    cur = conn.cursor()
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    member = ctx.message.author
    cur.execute("INSERT INTO logs(name, id, cause, time, unix_time) VALUES(?, ?, ?, ?, ?)", (member.name, member.id, str(error), time, int(now.timestamp()),))
    if isinstance(error, commands.CommandNotFound):
        cur.execute(f"SELECT lang FROM users WHERE id = ?", (member.id,))
        data = cur.fetchone()
        if not data:
            cur.execute(f"INSERT INTO users(name, id, lang) VALUES(?, ?, ?)", (member.name, member.id, 'en',))
            cur.execute(f"SELECT lang FROM users WHERE id = ?", (member.id,))
            data = cur.fetchone()

        await ctx.send(get_locale(data[0], "command_not_found"))
    else:
        await ctx.send("Whoops! I ran into an error! Nobu-kun check my log please!")
    cur.close()

@client.command()
async def credits(ctx):
    message = ctx.message
    author = message.author
    cur = conn.cursor()
    cur.execute("SELECT lang FROM users WHERE id = ?", (author.id,))
    data = cur.fetchone()
    if not data:
        cur.execute("INSERT INTO users(name, id, lang) VALUES(?, ?, ?)", (author.name, author.id, 'en',))
        cur.execute("SELECT lang FROM users WHERE id = ?", (author.id,))
        data = cur.fetchone()
    cur.close()

    title = get_locale(data[0], "credits_command_title")
    embed = discord.Embed(title=f"Rin Rin ❤ {title}", color=2367979)
    embed.add_field(name=get_locale(data[0], "bot_developer"), value="Nobuyaki#4974", inline=True)
    embed.add_field(name=get_locale(data[0], "bot_assistant_developer"), value="Pineapple_Cookie (美波🌊 fan)#0373", inline=True)
    embed.add_field(name=get_locale(data[0], "russian_translation"), value="Pineapple_Cookie (美波🌊 fan)#0373", inline=False)
    embed.add_field(name=get_locale(data[0], "lithuanian_translation"), value="uwu#1337 & Nexurent#6458", inline=True)
    embed.add_field(name=get_locale(data[0], "lithuanian_quality_check"), value="Nexurent#6458", inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=['?','h'])
async def help(ctx):
    message = ctx.message
    author = message.author

    cur = conn.cursor()
    cur.execute("SELECT lang FROM users WHERE id = ?", (author.id,))
    data = cur.fetchone()
    if not data:
        cur.execute("INSERT INTO users(name, id, lang) VALUES(?, ?, ?)", (author.name, author.id, 'en',))
        cur.execute("SELECT lang FROM users WHERE id = ?", (author.id,))
        data = cur.fetchone()
    cur.close()

    userlang = data[0]

    startnumber = get_locale(userlang, 'startnumber')
    endnumber = get_locale(userlang, 'endnumber')
    embed = discord.Embed(title="Rin Rin ❤ " + get_locale(userlang, "help_command_title"), description=BotVersion, color=2367979)
    embed.add_field(name="rr.help", value=get_locale(userlang, "help_command_help"), inline=False)
    embed.add_field(name=f"rr.rn ({startnumber}) ({endnumber})", value=get_locale(userlang, "help_command_rn"), inline=False)
    embed.add_field(name="rr.match (name) (partner)", value=get_locale(userlang, "help_command_match"), inline=False)
    embed.add_field(name="rr.ping", value=get_locale(userlang, "help_command_ping"), inline=False)
    embed.add_field(name="rr.info", value=get_locale(userlang, "help_command_info"), inline=False)
    embed.add_field(name="rr.lang (en/lt/ru)", value=get_locale(userlang, "help_command_lang"))
    embed.add_field(name="rr.credits", value=get_locale(userlang, "help_command_credits"), inline=False)
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Rin Rin ❤ Info", description="About me!", color=8993300)
    embed.add_field(name="Bot Author:", value="Nobuyaki#4974", inline=False)
    embed.add_field(name="Bot Version:", value=BotVersion, inline=False)
    embed.add_field(name="Github Link:", value="https://github.com/liberation4you/rinrindiscord", inline=False)
    embed.set_footer(text="Rin Rin ❤", icon_url="https://avatars1.githubusercontent.com/u/53136821?s=400&u=7877010f24ed4d436db5f1c6aa559fde428dcb31&v=4")
    await ctx.send(embed=embed)

@client.command()
async def lang(ctx, language: str="en"):
    message = ctx.message
    author = message.author

    language = language.lower()
    if not language in all_languages.values():
        language = all_languages.get(language, "en")

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (author.id,))
    data = cur.fetchone()
    if not data:
        cur.execute("INSERT INTO users(name, id, lang) VALUES(?, ?, ?)", (author.name, author.id, language,))
    else:
        cur.execute("UPDATE users SET lang = ? WHERE id = ?", (language, author.id,))
        conn.commit()
    cur.close()

    await ctx.send(get_locale(language, "lang_response"))


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
        await ctx.send("You need to enter two numbers!")

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
