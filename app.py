import discord
from discord.ext import commands
from discord import Color   
import os
import requests
from bs4 import BeautifulSoup

token = os.getenv("TOKEN")

intents = discord.Intents.all()  # or .all() if you ticked all, that is easier

client = commands.Bot(command_prefix="p!", intents=intents)


@client.event
async def on_ready():
    print("Polygon Bot Initialized!")


@client.event
async def on_member_join(member):
    count = len([m for m in member.guild.members if not m.bot])
    channel = client.get_channel("")
    await channel.edit(name=f"Member Count: {count}")

@client.event
async def on_member_leave(member):
    count = len([m for m in member.guild.members if not m.bot])
    channel = client.get_channel(1037055015912742952)
    await client.edit_channel(channel, f"Member Count: {count}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def links(ctx):
    embed = discord.Embed(
        title="-Official Links-",
        description="Here are the official links for **'Polygon Assets'**:",
        color=Color.dark_gold())
    embed.set_author(
        name="Polygon Assets",
        icon_url="https://cdn.discordapp.com/avatars/1036736644969144390/5187c207a99226c0367a3cff65944b00.webp?size=64"
    )
    embed.set_footer(text="💛")

    embed.add_field(name="Official Website",
                    value="**https://www.polygonasset.net/** \n",
                    inline=False)
    embed.add_field(name="Youtube & Tutorials", value="Soon! \n", inline=False)
    embed.add_field(name="Documentation", value="Soon! \n", inline=True)

    await ctx.channel.purge(limit=1)
    message = await ctx.channel.send(embed=embed)
    await message.add_reaction("✅")

    def check(reaction, user):  # Our check for the reaction
        return user == ctx.message.author

    reaction = await client.wait_for("reaction_add", check=check)
    await message.delete()


@client.command(aliases=['commands'])
async def coms(ctx):
    embed = discord.Embed(
        title="-Commands-",
        description="Here are the bot commands for **'Polygon Assets'**:",
        color=Color.blue())
    embed.set_author(
        name="Polygon Assets",
        icon_url="https://cdn.discordapp.com/avatars/1036736644969144390/5187c207a99226c0367a3cff65944b00.webp?size=64"
    )
    embed.set_footer(text="💜")

    embed.add_field(name="p!commands",
                    value="Lists the available commands. \n",
                    inline=False)
    embed.add_field(name="p!verify", value="Soon! \n", inline=False)
    embed.add_field(name="p!links",
                    value="Lists the official links. \n",
                    inline=True)

    await ctx.channel.purge(limit=1)
    message = await ctx.channel.send(embed=embed)
    await message.add_reaction("✅")

    def check(reaction, user):  # Our check for the reaction
        return user == ctx.message.author

    reaction = await client.wait_for("reaction_add", check=check)
    await message.delete()


@client.command()
@commands.has_permissions(administrator=True)
async def reviews(ctx, link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    souped = str(soup.findAll('div')).split("</div>")
    nameS = str(str(soup.find_all("h1")).split('">')[1]).split("</h1")[0]
    print(soup.find_all("h1"))
    await ctx.message.delete()
    for st in souped:
        if str(st).find('class="NoXio"') > 0 and str(st).find('">(') > 0:
            new_st = str(st).split('">')[1]
            await ctx.send(f"**{nameS}'s** Review Count: {new_st}")
            return
    await ctx.send("Couldn't retrieve the reviews!")


@client.command()
@commands.has_permissions(administrator=True)
async def create(ctx, Title, Desc):
    embed = discord.Embed(title=Title, description=Desc, color=Color.red())
    embed.set_thumbnail(
        url="https://creazilla-store.fra1.digitaloceanspaces.com/emojis/42846/megaphone-emoji-clipart-xl.png"
    )
    embed.set_author(
        name=ctx.message.author.name,
        icon_url="https://cdn.discordapp.com/avatars/1036736644969144390/5187c207a99226c0367a3cff65944b00.webp?size=64"
    )
    embed.set_footer(text=f"New Announcement By: {ctx.message.author.name}")

    channel = client.get_channel(1036689705401593916)
    await channel.send(ctx.message.guild.default_role)
    message = await channel.send(embed=embed)
    await message.add_reaction("🔥")
    await ctx.channel.purge(limit=1)


client.run(token)
