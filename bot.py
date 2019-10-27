import discord
import random
import os
from datetime import datetime
from discord.ext import commands

BotVersion = "v 10.27.19.7p"
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
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    log = open("log", "a")
    log.write(f"\nError: {time} | MemberID: {ctx.message.author.id} caused: {error}")
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
                if memlanguage == "ru":
                    languageCheck.close()
                    await ctx.send("Команда не найдена! Проверьте, может это опечатка!")
                else:
                    languageCheck.close()
                    await ctx.send("Komanda nerasta! Patikrinkite ar tai buvo rašybos klaida!")

        else:
            languageCreate = open(f"memlangs\{member}", "w+")
            languageCreate.write("en")
            languageCreate.close()
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            log = open("log", "a")
            log.write(f"\nLog: {time} | MemberID: {ctx.message.author.id}: Member didn't have a language file, created one via NotACommand Error!")
            log.close()
            print(f"Rin Rin TempLog/CommandNotFound> {member} didn't have a lang file! Creating one.")
            await ctx.send("Command not found! Check to see if it was a typo!")
    else:
            await ctx.send("Whoops! I ran into an error! Nobu-kun check my log please!")

@client.command()
async def credits(ctx):
    embed = discord.Embed(title="Rin Rin ❤ Credits", color=2367979)
    embed.add_field(name="Bot Developer", value="Nobuyaki#4974")
    embed.add_field(name="Russian Translation", value="Pineapple_Cookie (美波🌊 fan)#0373", inline=False)
    embed.add_field(name="Lithuanian Translation", value="uwu#1337 and Nexurent#6458", inline=False)
    embed.add_field(name="Lithuanian Translation Quality Checker", value="Nexurent#6458", inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['?','h'])
async def help(ctx):
    member = ctx.message.author.id
    if os.path.exists(f"memlangs\{member}"):
        languageCheck = open(f"memlangs\{member}", "r")
        userlang = languageCheck.read()
        if userlang == "en":
            languageCheck.close()
            embed = discord.Embed(title="Rin Rin ❤ Help", description=BotVersion, color=2367979)
            embed.add_field(name="rr.help", value="Shows this message", inline=False)
            embed.add_field(name="rr.rn (startnumber)(endnumber)", value="Gets a random number from start to end.", inline=False)
            embed.add_field(name="rr.match (name) (partner)", value="Calculates compatibility with name and partner.", inline=False)
            embed.add_field(name="rr.ping", value="Shows my ping!", inline=False)
            embed.add_field(name="rr.info", value="Shows bot info!", inline=False)
            embed.add_field(name="rr.lang (en/lt/ru)", value="Changes bot's language!")
            embed.add_field(name="rr.credits", value="Shows credits!", inline=False)
            await ctx.send(embed=embed)
        else:
            if userlang == "ru":
                languageCheck.close()
                embed = discord.Embed(title="Rin Rin ❤ Помощь", description=BotVersion, color=2367979)
                embed.add_field(name="rr.help", value="Показать это сообщение.", inline=False)
                embed.add_field(name="rr.rn (старт) (стоп)", value="Получить случайное число от старт до стоп.", inline=False)
                embed.add_field(name="rr.match (имя) (партнер)", value="Посчитать совместимость имени и партнера.", inline=False)
                embed.add_field(name="rr.ping", value="Показать мой пинг!", inline=False)
                embed.add_field(name="rr.info", value="Показать информацию о боте!", inline=False)
                embed.add_field(name="rr.lang (en/lt/ru)", value="Changes bot's language!")
                embed.add_field(name="rr.credits", value="Shows credits!", inline=False)
                await ctx.send(embed=embed)
            else:
                if userlang == "lt":
                    languageCheck.close()
                    embed = discord.Embed(title="Rin Rin❤ Pagalba", description=BotVersion, color=2367979)
                    embed.add_field(name="rr.help", value="Parodo šitą žinutę", inline=False)
                    embed.add_field(name="rr.rn (pradinisnumeris) (paskutinisnumeris)", value="Parodo generuota numerį nuo pradinio numerio iki paskutinio.", inline=False)
                    embed.add_field(name="rr.match (vardas) (partneris)", value="Suskaičiuoja kiek vardas ir partneris tinka.", inline=False)
                    embed.add_field(name="rr.ping", value="Parodo mano pingą!", inline=False)
                    embed.add_field(name="rr.info", value="Parodo boto informaciją!", inline=False)
                    embed.add_field(name="rr.lang (en/lt/ru)", value="Changes bot's language!")
                    embed.add_field(name="rr.credits", value="Shows credits!", inline=False)
                    await ctx.send(embed=embed)
    else:
        languageCreate = open(f"memlangs\{member}", "w+")
        languageCreate.write("en")
        languageCreate.close()
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        log = open("log", "a")
        log.write(
            f"\nLog: {time} | MemberID: {ctx.message.author.id}: Member didn't have a language file, created one via Help Command!")
        log.close()
        print(f"Rin Rin TempLog/CommandNotFound> {member} didn't have a lang file! Creating one.")
        embed = discord.Embed(title="Rin Rin ❤ Help", description=BotVersion, color=2367979)
        embed.add_field(name="rr.help", value="Shows this message", inline=False)
        embed.add_field(name="rr.rn (startnumber)(endnumber)", value="Gets a random number from start to end.", inline=False)
        embed.add_field(name="rr.match (name) (partner)", value="Calculates compatibility with name and partner.", inline=False)
        embed.add_field(name="rr.ping", value="Shows my ping!", inline=False)
        embed.add_field(name="rr.info", value="Shows bot info!", inline=False)
        embed.add_field(name="rr.lang (en/lt/ru)", value="Changes bot's language!")
        embed.add_field(name="rr.credits", value="Shows credits!", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Rin Rin ❤ Info", description="About me!", color=8993300)
    embed.add_field(name="Bot Author:", value="Nobuyaki#4974", inline=False)
    embed.add_field(name="Bot Version:",value=BotVersion, inline=False)
    embed.add_field(name="Github Link:", value="https://github.com/liberation4you/rinrindiscord", inline=False)
    embed.set_footer(text="Rin Rin ❤",icon_url="https://avatars1.githubusercontent.com/u/53136821?s=400&u=7877010f24ed4d436db5f1c6aa559fde428dcb31&v=4")
    await ctx.send(embed=embed)

@client.command()
async def lang(ctx, language: str = None):
    memberID = ctx.message.author.id
    if language == "en":
        file = open(f"memlangs\{memberID}", "w+")
        file.write("en")
        await ctx.send(f"Changed your language to **English**!")
        file.close()
    else:
        if language == "ru":
            file = open(f"memlangs\{memberID}", "w+")
            file.write("ru")
            await ctx.send(f"Ваш язык изменён на **Русский**!")
            file.close()
        else:
            if language == "lt":
                file = open(f"memlangs\{memberID}", "w+")
                file.write("lt")
                await ctx.send(f"Kalba pakeista į **Lietuvių**!")
            else:
                if language is None:
                    if os.path.exists(f"memlangs\{memberID}"):
                        file = open(f"memlangs\{memberID}", "r")
                        currentlang = file.read()
                        if currentlang == "en":
                            await ctx.send("Your current language is **English**!")
                            file.close()
                        else:
                            if currentlang == "ru":
                                await ctx.send("Ваш текущий язык **Русский**!")
                                file.close()
                            else:
                                if currentlang == "lt":
                                    await ctx.send("Tavo dabartinė kalba yra **Lietuvių**!")
                                    file.close()
                    else:
                        languageCreate = open(f"memlangs\{member}", "w+")
                        languageCreate.write("en")
                        languageCreate.close()
                        now = datetime.now()
                        time = now.strftime("%H:%M:%S")
                        log = open("log", "a")
                        log.write(f"\nLog: {time} | MemberID: {ctx.message.author.id}: Member didn't have a language file, created one via Language Command!")
                        log.close()
                        print(f"Rin Rin TempLog/FileNotFound> {member} didn't have a lang file! Creating one.")
                        await ctx.send(f"You don't have a lang file so I made you one! Default language is **English**.\nType rr.lang again to see language.")

                else:
                    await ctx.send("Incorrect language! Type 'en' for English, 'ru' for Russian, and 'lt' for Lithuanian.")

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
