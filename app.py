import discord
from discord.ext import commands
from discord import Color   

token = "MTAzODEzNzMwODE5MDM1MTQzMg.GlOBYO.5DVOqxzzgu6EJFm9WaXOFFuPCEJJxDudKCLOGI"

intents = discord.Intents.all()  # or .all() if you ticked all, that is easier

client = commands.Bot(command_prefix="p!", intents=intents)


@client.event
async def on_ready():
    print("Polygon Bot Initialized!")


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
