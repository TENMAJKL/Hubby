import requests

class Organization:

	# Static
	

	@staticmethod
	def find(name:str):
		res = requests.get(f"https://api.github.com/orgs/{name}")

		if res.status_code == 404:
			return "Not found"
		if res.status_code != 200:
			return "Uncaught error"
		
		data = res.json()

		return Organization(
			data["login"],
			data["name"],
			data["html_url"],
			data["avatar_url"],
			data["description"],
			data["public_repos"],
			data["blog"],
			data["followers"],
			data["following"]
		)

	def __init__(self, login, name, url, avatar_url, description, repos, web, followers, following):
		self.login = login
		self.name = name if name else login
		self.url = url
		self.avatar_url = avatar_url
		self.description = description
		self.repos = repos
		self.web = web
		self.followers = followers
		self.following = following