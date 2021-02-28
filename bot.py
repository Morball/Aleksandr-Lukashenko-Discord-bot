import asyncio
import collections
import discord
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import random
from discord import User
from discord.ext.commands import has_permissions
import string
import socket
import os
from pprint import pprint
from discord.ext.commands import has_permissions
client = commands.Bot(command_prefix=".")



@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")
    
    
    
@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")
    
    
    
    
    
@client.command(aliases=["8ball"])
async def _8ball(ctx, * ,question):
    resp=["yes", "no"]
    emb=discord.Embed(title="8Ball", color=0xfcba03)
    emb.add_field(name="Response", value=random.choice(resp)) 
    await ctx.send(embed=emb)
    await ctx.send(ctx.message.author.id)

    
    
@client.command()
async def latency(ctx):
    lat=discord.Embed(title="Bot's latency")
    skr=client.latency*1000
    lat.add_field(name="Current latency", value=f"{skr} ms")
    await ctx.send(embed=lat)
    
    
    
    
@client.command()
@has_permissions(administrator=True)
async def cc(ctx):
    await ctx.channel.purge()   
    
    
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    b=discord.Embed(title=f"Banned case", color=0xfcba03)
    b.add_field(name=f"Banned member {member}", value="Reason: {reason}", inline=False)
    await ctx.send(embed=b)
    
    
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user


    
@client.command()
async def tag(ctx, *, name):    
    if name == "tias":
        await ctx.send("https://images-ext-1.discordapp.net/external/wS10LdHIWkTJUPw5VOvHt_DYTpJzXgT9R1T0L80BfX0/https/images-ext-2.discordapp.net/external/cMwYUbpT0hlBUSj1Hl96rZbjvYGiiuhtUaoZT4cTRuY/https/i.imgur.com/VkRzeQJ.png")
    elif name == "trans":
        await ctx.send("https://cdn.discordapp.com/attachments/757703481552404631/812250895030157342/Trans_Rights.mov")
    elif name == "dox":
        await ctx.send("https://media.discordapp.net/attachments/773871630337441822/814045887261048852/image0.jpg?width=676&height=676")
    elif name == "baguette":
        await ctx.send("https://media.tenor.co/videos/ec3aed6d6cb99cc3e4ef789cef227836/mp4")
        
        
        
    
@client.command()
async def check(ctx, host):
    check=discord.Embed(title=f"Checked host {host}", color=0xfcba03)
    on = True if os.system(f"ping {host}") == 0 else False
    if on==True:
       check.add_field(name="Host is up and running!", value="Nice")
    else:
       check.add_field(name="Host is unreachable...", value="Not Nice")
    await ctx.send(embed=check)
    
    
    
        
client.remove_command('help')

        
@client.command() 
async def help(ctx):
    tools = discord.Embed(title="Help", 
        color=0xfcba03)
    tools.add_field(name="Prefix", value="▸ .", inline=False)
    tools.add_field(name="Portscan", value="▸ Port scaner", inline=False)
    tools.add_field(name="Geo", value="▸ Ip address information", inline=False)
    tools.add_field(name="Check", value="▸ Checks if a host is up or down", inline=False)
    tools.add_field(name="8ball", value="▸ 8ball", inline=False)
    tools.add_field(name="Ban", value="▸ Ban Someone (Admins only)", inline=False)
    tools.add_field(name="Latency", value="▸ Checks the latency of the bot", inline=False)
    tools.add_field(name="Btcprice", value="▸ Checks current Bitcoin price (may be a little off)", inline=False)
    tools.add_field(name="Tag (tias, trans, dox, baguette)", value="▸ Cached images", inline=False)
    tools.add_field(name="Changelog", value="▸ Displays changelog", inline=False)
    tools.add_field(name="Help", value="▸ Displays this message", inline=False)
    
    await ctx.send(embed=tools)
    
    
    
    
@client.command()
async def rules(ctx):
    rules = discord.Embed(title="Rules", 
        color=0xfcba03)
    rules.add_field(name="Attacking goverment websites", value="Is [STRICTLY] prohibited and you will be removed (or banned) from the server (we won't get in trouble, you will)", inline=False)
    rules.add_field(name="Disrespecting the Owner(s) or Admin(s)", value="Is prohibited and you will be removed (or banned) from the server", inline=False)
    rules.add_field(name="Breaking the rules", value="Is prohibited and you will be removed (or banned) from the server", inline=False)
    rules.add_field(name="Spam", value="Is prohibited and you will be removed (or banned) from the server", inline=False)
    rules.add_field(name="Trashtalking", value="Is prohibited and you will be removed (or banned) from the server", inline=False)
    rules.add_field(name="Abusing any bug found", value="Is prohibited and you will be removed (or banned) from the server", inline=False)
    await ctx.send(embed=rules) 
    
    '''MAKE UP SOME BETTER RULES RETARD'''
    
    
@client.command()
async def portscan(ctx, ip):
    usr=ctx.author
    ebd=discord.Embed(title=f"Scanning ports on {ip}", color=0xfcba03)
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nono=0
    for i in range(1, 1025):
        result=sock.connect_ex((ip, i))
        if result == 0:
            ebd.add_field(name="OPEN PORT FOUND", value=f"{i} is open.", inline=False)
            nono+=1
        else:
            pass
        if nono==0:
            ebd.add_field(name="No open ports found", value="bit sad", inline=False )
    usr.mention
    await ctx.send(embed=ebd)

@client.command()
async def geo(ctx, ip):
    
    geoipembed=discord.Embed(title="IP GEO", color=0xfcba03)
    #https://ipapi.co/8.8.8.8/json/
    req=requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey=2faf3dc5e6f04b079afe310e430a63fd&ip={ip}")
    jason=json.loads(req.text)
    geoipembed.add_field(name="Ip address", value=jason['ip'], inline=False)
    geoipembed.add_field(name="Country", value=jason['country_name'], inline=False)
    geoipembed.add_field(name="Region", value=jason['state_prov'], inline=False)
    geoipembed.add_field(name="City", value=jason['city'], inline=False)
    geoipembed.add_field(name="ISP", value=jason['isp'], inline=False)
    geoipembed.add_field(name="ZIP", value=jason['zipcode'], inline=False)
    geoipembed.add_field(name="Latitude", value=jason['latitude'], inline=False)
    geoipembed.add_field(name="Longitude", value=jason['longitude'], inline=False)
    
    #https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8
    
    await ctx.send(embed=geoipembed)
    

@client.command()
async def btcprice(ctx):
    jason=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    njson=json.loads(jason.text)
    skrr=njson['bpi']
    skr=skrr['EUR']
    PRICE=skr['rate'] 
    bed=discord.Embed(title="Current Bitcoint price", color=0xfcba03)
    bed.add_field(name=f"Current bitcoin price in euro is at", value=f"€{PRICE}", inline=False)
    
    await ctx.send(embed=bed)


@client.command()
async def changelog(ctx):
    bed=discord.Embed(title="Changelog", color=0xfcba03)
    bed.add_field(name="Last update: 24/02/2021", value="Changes:\n ▸ Changed the ip geolocation API \n ▸ Improved the port scanner \n ▸ Added a BTC price checker \n", inline=False )
    bed.add_field(name="What to expect from future updates", value="▸ Fuzzing tools \n ▸ Better menus \n ▸ A paid ddos tool ", inline=False )
    await ctx.send(embed=bed)
    
    
    

    
    
    
    
    
    
    
    
    
    
client.run("YOUR_TOKEN")    


