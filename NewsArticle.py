from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

#soup = BeautifulSoup(html_doc, 'html.parser')

class NewsArticle(object):
	def __init__(self, title, summary, article_url, article_original_url, pub_date):
		self.title = title;
		self.summary = summary;
		self.article_url = article_url
		self.article_original_url = article_original_url
		self.pub_date = self.to_datetime(pub_date)
		#self.crawl_naver_news_page()

	def __repr__(self):
		return self.title + ' (' + self.pub_date.strftime("%Y. %m. %d.") + ')' + '\n' + self.summary

	def to_datetime(self, pub_date):
		return datetime.strptime(pub_date, "%a, %d %b %Y %X %z")

	def crawl_naver_news_page(self):
		r = urlopen(self.article_url).read()
		soup = BeautifulSoup(r, 'html.parser')
		print(soup.find_all('span', class_='u_cbox_count'))