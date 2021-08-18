import discord
import os
from keep_alive import keep_alive

from discord.ext import commands
from dotenv import load_dotenv




intents = discord.Intents().default()
intents.members = True
intents.presences = True
intents.reactions = True
client = commands.Bot(command_prefix = "$", intents=intents)
client.remove_command("help")
load_dotenv()
TOKEN = os.getenv('TOKEN')



@client.event  
async def on_ready():
	print("-------------------------")
	print("Bot Name: " + client.user.name)
	print(client.user.id)
	print("API Version: " + discord.__version__)
	print(client.latency * 1000)
	print("-------------------------")

	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your GitHub stats"))




for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


keep_alive()
client.run(TOKEN)
