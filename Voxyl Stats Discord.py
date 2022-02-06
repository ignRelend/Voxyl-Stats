import discord, image, voxyl_api
from discord.ext import commands
from discord_slash import SlashCommand
from PIL import Image

file = open('token.txt','r')
token = file.readline(255)
file.close()

def create_embed(top, desc):
    embed = discord.Embed(
        title = top,
        description = desc,
        colour = discord.Colour.green()
    )
    embed.set_footer(text="https://discord.gg/bwp")
    return embed

client = commands.Bot(command_prefix=".", help_command=None, activity = discord.Game(name="voxyl.net"))
slash = SlashCommand(client=client, sync_commands=True)

@client.event
async def on_ready():
    guild_total = 0
    print("Ready!")
    for guild in client.guilds:
        guild_total += 1
    print("Current Guilds (" + str(guild_total) + "):")
    for guild in client.guilds:
        print(guild.name + " - " + str(guild.id))
    print()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        return

@slash.slash(name="profile", description="Search for any player's stats")
async def profile(ctx, name, game=None):
    await stats(ctx, name, game)

@slash.slash(name="stats", description="Search for any player's stats")
async def stats(ctx, name, game=None):
    uuid = voxyl_api.name_to_uuid(name)
    name = voxyl_api.uuid_to_name(uuid)
    gen = await ctx.send("Generating image...")
    if game == None:
        try:
            image.create_stats_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "bbf":
        try:
            image.create_bbf_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Bed Bridge Fight stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Bed Brige Fight stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "bbf2":
        try:
            image.create_bbf2_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Bed Bridge Fight Doubles stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Bed Brige Fight Doubles stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "vf":
        try:
            image.create_vf_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Void Fight stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Void Fight stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "vf2":
        try:
            image.create_vf2_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Void Fight Doubles stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Void Fight Doubles stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "sf":
        try:
            image.create_sf_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Stick Fight stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Stick Fight stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "sf2":
        try:
            image.create_sf2_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Stick Fight Doubles stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Stick Fight Doubles stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "pf":
        try:
            image.create_pf_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Pearl Fight stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Pearl Fight stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "pf2":
        try:
            image.create_pf2_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Pearl Fight Doubles stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Pearl Fight Doubles stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "sumo" or game == "bs":
        try:
            image.create_sumo_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Block Sumo stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Block Sumo stats failed to load for " + str(ctx.message.author) + ".")
    elif game == "bbs" or game == "betasumo":
        try:
            image.create_betasumo_image(name)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {name}'s Beta Block Sumo stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{name}'s Beta Block Sumo stats failed to load for " + str(ctx.message.author) + ".")
    else:
        await ctx.channel.send("That is not a valid gamemode.\nRun .help to see all gamemodes.")
    await gen.delete()

@slash.slash(name="guild", description="Search for any guild's stats")
async def guild(ctx, tag):
    if tag != "top":
        tag = tag.upper()
        try:
            image.create_guild_image(tag)
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print(f"Sent {tag}'s Guild stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print(f"{tag}'s Guild stats failed to load for " + str(ctx.message.author) + ".")
    elif tag == "top":
        try:
            image.create_guild_image_top()
            await ctx.channel.send(file=discord.File('assets/finish.png'))
            print("Sent Top Guild stats to " + str(ctx.message.author) + ".")
        except discord.ext.commands.errors.CommandInvokeError or Image.UnidentifiedImageError:
            await ctx.channel.send("Please try again, loading data.")
            print("Top Guild stats failed to load for " + str(ctx.message.author) + ".")

@slash.slash(name="help", description="The help command")
async def help(ctx):
    await ctx.send(embed=create_embed("Voxyl Stats Help", "Voxyl Stats is developed by Relend as an easy way to view other player's stats.\n\n**Available Commands:**\n"
    ".stats <player> [mode] - Used to find a player's statistics in a gamemode\n"
    ".profile <player> [mode] - Used to find a player's statistics in a gamemode\n"
    ".guild <tag|top> - Used to find a guild's statistics or top guilds\n\n"
    "**Available Modes:**\n"
    "bbf - Bed Bridge Fight Solo\nbbf2 - Bed Bridge Fight Doubles\n"
    "vf - Void Fight Solo\nvf2 - Void Fight Doubles\n"
    "sf - Stick Fight Solo\nsf2 - Stick Fight Doubles\n"
    "pf - Pearl Fight Solo\npf2 - Pearl Fight Doubles\n"
    "bs - Block Sumo\nbbs - Beta Block Sumo\n\n"
    "DM <@497411369214410753> for inquiries related to this bot."))
    print("Send the help message to " + str(ctx.message.author) + ".")

client.run(token)