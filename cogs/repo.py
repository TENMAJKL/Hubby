import discord
from discord.ext import commands
from Models.Repository import Repository
from data import colors

client = discord.Client()


class RepositoryCog(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("️Repository commands - ✔️ ")

	@commands.command()
	@commands.cooldown(rate=1, per=30)
	async def repo(self, ctx, owner:str, name:str):
		repo = Repository.find(owner, name)
		color = colors[repo.language].replace("#", "0x")
		embed=discord.Embed(color=int(color, 0), title=repo.name, description=repo.description, url=repo.url)
		embed.add_field(name="Language", value=repo.language)
		embed.add_field(name="Stars", value=repo.stars)
		embed.add_field(name="Forks", value=repo.forks)

		embed.set_author(name=repo.owner.name, icon_url=repo.owner.avatar_url, url=repo.owner.url)

		await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RepositoryCog(client))

