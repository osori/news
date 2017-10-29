import json, requests
from .NewsArticle import NewsArticle
import datetime
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict



CLIENT_ID = 'KD8LEwXEMSZ1wibV6rcE'
CLIENT_SECRET = 'GlIChciyle'
API_URL = 'https://openapi.naver.com/v1/search/news.json'

class NaverNews(object):
	def __init__(self, query):
		self.query = query
		self.article_list = []
		self.articles_by_date = defaultdict(list)
		self.top3_dict = {}

	def fetch_articles(self):
		# Make an API Call
		headers = { 'X-Naver-Client-Id': CLIENT_ID,
					'X-Naver-Client-Secret': CLIENT_SECRET
		}
		params = { 	'query': self.query,
					'display': 100,
					'start': 1,
					'sort': 'sim'
		}


		response = requests.get(API_URL, headers=headers, params=params)
		json = response.json()

		num_articles = json['total']
		print("total num of articles:", num_articles)

		# Make a list of NewsArticles
		for item in json['items']:
			news_article = NewsArticle(item['title'], item['description'], item['link'], item['originallink'], item['pubDate'])
			self.article_list.append(news_article)
		#return self.article_list

		# Return articles 

	def sort_by_time(self, order_by):
		if order_by == None: order_by = 'desc'
		self.article_list = sorted(self.article_list, key=lambda x: x.pub_date, reverse=True if order_by=='desc' else False)


	def plot_time_trend(self):
		# Categorize articles into dates
		for article in self.article_list:
			article_date = article.pub_date.date()
			self.articles_by_date[article_date].append(article)

		# sort the dates by descending order
		sorted_dates = sorted(self.articles_by_date, key=lambda k: len(self.articles_by_date[k]), reverse=True)
		
		# dict that stores (date, # of articles)
		date_count_pair = {}
		for d in sorted_dates[:3]:
			date_count_pair[d] = len(self.articles_by_date[d])
		print(date_count_pair)
		self.top3_dict = date_count_pair

		return date_count_pair


	def get_top_topics(self):
		top_topics = ['윤송이 부친 살해', '홍준표 서청원 녹취록', '한국당 보이콧', '홍종학 불법 증여', '카탈루냐 지방', '풍계리 핵실험']
		return top_topics


"""
def main():
	n = NaverNews()
	n.fetch_articles()
	n.sort_by_time('asc')
	for i in n.article_list:
		print("*",i)
	#print(items[0].pub_date)

if __name__ == "__main__":
    main()

"""