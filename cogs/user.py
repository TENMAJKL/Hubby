import discord
from discord.ext import commands
from Models.User import User

client = discord.Client()


class UserCog(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("User commands - ✔️ ")

	@commands.command()
	@commands.cooldown(rate=1, per=30)
	async def user(self, ctx, name:str):
		user = User.find(name)
		embed=discord.Embed(color=0x000000, title=user.web, description=user.bio, url=user.web)
		embed.add_field(name="Company", value=user.company)
		embed.add_field(name="Repositories", value=user.repos)
		embed.add_field(name="Followers", value=user.followers)
		embed.add_field(name="Following", value=user.following)

		embed.set_author(name=user.name, icon_url=user.avatar_url, url=user.url)
		await ctx.send(embed=embed)

def setup(client):
    client.add_cog(UserCog(client))