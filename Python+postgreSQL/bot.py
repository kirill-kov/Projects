import discord
from discord.ext import commands
from tensordb import dbConnection
from asyncio import sleep

data = dbConnection()
first_table = data.size_table()
second_table = data.size_table2()


TOKEN = "NTYxNDk2OTQ0Njc0MDc4NzMw.XJ9FGw.LkcfYOT6rxOh--sgpduJt6q8OEA"
bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print("Bot is ready")

bot.remove_command('help')

@bot.command(pass_context = True)
async def pet(ctx):
    await ctx.send(first_table)

@bot.command(pass_context = True)
async def people(ctx):
    await ctx.send(second_table)

@bot.command(pass_context = True)
async def start(ctx, n:int):
    while True:
        await ctx.send(first_table)
        await ctx.send(second_table)
        await sleep(n)

@bot.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title="Tensor bot", description="List of commands are:", color=0x8E7CC3)

    embed.add_field(name="$start", value="Start auto parsing size tables in DB (enter the N sec)", inline=False)
    embed.add_field(name="$pet ", value="Gives the size of table 'Pet' in DB", inline=False)
    embed.add_field(name="$people ", value="Gives the size of table 'People' in DB", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
