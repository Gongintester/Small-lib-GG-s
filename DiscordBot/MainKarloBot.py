from math import cos
import discord
from discord.ext import commands, tasks
import GonginLib
import GonginsServerLib


#Data Varibels

BOT_TOKEN = ""
CHANNEL_ID = jedid = 1181491021595549709


BotInfo = open("Pl_Info.lang", "r", encoding='UTF-8')
TexBI = BotInfo.read()
Pluse = open("ascii-art.txt", "r", encoding='UTF-8')
PluseText = Pluse.read()

#Command settings
TlumBot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Test function dev command
@TlumBot.command() 
async def testdevfun(tev):
    await tev.send("ci w")
    return

@TlumBot.command() 
async def helpbot(tev):
    await tev.send(TexBI)
    return

#krypt and unkrypt command
@TlumBot.command()
async def Z (ctx, *, args):
    if (args[0]) == "K" or (args[0]) == "k":
        await ctx.send("``` " +  (GonginLib.NewEncrypting(args[2:],"")) + "```") 
    elif (args[0]) == "U" or (args[0]) == "u":
        await ctx.send("``` " + (GonginLib.Uncrypting(args[2:])) + "```")
    else:
        await ctx.send("NO K#RWA CO TY MI WYSY#ASZ")
    return

@TlumBot.command()
async def z (ctx, *, args):
    if (args[0]) == "K" or (args[0]) == "k":
        await ctx.send("``` " +  (GonginLib.NewEncrypting(args[2:],"")) + "```") 
    elif (args[0]) == "U" or (args[0]) == "u":
        await ctx.send("``` " + (GonginLib.Uncrypting(args[2:])) + "```")
    else:
        await ctx.send("NO K#RWA CO TY MI WYSY#ASZ")
    return

@TlumBot.command()
async def ser (ctx, *, args):
    await ctx.send(GonginsServerLib.getServer(args))
    return

TlumBot.run(BOT_TOKEN)

