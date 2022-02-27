import discord
import os
from discord.ext import commands

TOKEN = "Your bot token"
PREFIX = "Your bot prefix"

bot = commands.AutoShardedBot(command_prefix=PREFIX)
bot.remove_command('help')

@bot.event
async def on_ready():
	print('Bot is ready')
	activity = discord.Activity(type=discord.ActivityType.listening, name=F"{PREFIX}help")
	await bot.change_presence(status=discord.Status.dnd, activity=activity)


@bot.event
async def on_message(message):
    if message.content == "hi":
        await message.channel.send("hello")


bot.run(TOKEN)