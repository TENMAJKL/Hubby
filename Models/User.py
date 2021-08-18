import requests

class User:

	# Static

	@staticmethod
	def find(name:str):
		res = requests.get(f"https://api.github.com/users/{name}")

		if res.status_code == 404:
			return "Not found"
		if res.status_code != 200:
			return "Uncaught error"
		
		data = res.json()

		return User(
			data["login"],
			data["name"],
			data["avatar_url"],
			data["html_url"],
			data["bio"],
			"http://"+data["blog"],
			data["company"],
			data["public_repos"],
			data["followers"],
			data["following"]
		)

	def __init__(self, login, name, avatar_url, url, bio, web, company, repos, followers, following):
		self.login = login
		self.name = name if name else login
		self.avatar_url = avatar_url
		self.url = url
		self.bio = bio
		self.web = web
		self.company = company
		self.repos = repos
		self.followers = followers
		self.following = following