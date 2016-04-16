__author__ = 'Jiarui Xu'


import requests
from bs4 import BeautifulSoup
import json

class DBpedia_BOT():
	def __init__(self):
		self.session = requests.Session()
		self.graph = 'http://dbpedia.org'
		self.format = 'application/json'

	def query_entity(self, wiki_title):
		query = self.query_constructor(wiki_title)
		response = self.session.get('http://dbpedia.org/sparql', \
						params={'default-graph-uri': self.graph, 'query': query, 'format': self.format})
		return response.json()

	def query_constructor(self, wiki_title):
		return 'DESCRIBE <http://dbpedia.org/resource/%s>' % (wiki_title,)
