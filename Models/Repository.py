import requests

from Models.User import User
from Models.Organization import Organization

class Repository:

	# Static

	@staticmethod
	def find(user:str, repo:str):
		res = requests.get(f"https://api.github.com/repos/{user}/{repo}")

		if res.status_code == 404:
			return "Not found"
		if res.status_code != 200:
			return "Uncaught error"
		
		data = res.json()
		owner = data["owner"]
		if owner["type"] == "Organization":
			author = Organization(
				owner["login"],
				owner["login"],
				owner["html_url"],
				owner["avatar_url"],
				""
				"", 
 				"", #Not nessesary to add and ints not also in this responce
				"",
				""
			)
		
		if owner["type"] == "User":
			author = User(
				owner["login"],
				owner["login"],
				owner["html_url"],
				owner["avatar_url"],
				"", 
 				"", #Not nessesary to add and ints not also in this responce
				"",
				""
			)

		return Repository(
			data["name"],
			author,
			data["description"],
			data["language"],
			data["license"]["name"],
			data["html_url"],
			data["stargazers_count"],
			data["forks_count"]
		)

	def __init__(self, name, owner, description, language, license, url, stars, forks):
		self.name = name
		self.owner = owner
		self.description = description
		self.language = language
		self.url = url
		self.stars = stars
		self.forks = forks
