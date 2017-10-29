from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.shortcuts import render

from news.NaverNews import NaverNews

# Create your views here.
class IndexView(TemplateView):
	template_name = "news/index.html"
	def get_context_data(self, **kwargs):
		top_topics = ['국정원 의혹', '한일관 대표 사망', '홍준표 서청원 녹취록', '한국당 보이콧', '홍종학 불법 증여', '카탈루냐 지방', '풍계리 핵실험', '윤송이', '경기 버스준공영제']
		context = super(IndexView, self).get_context_data(**kwargs)
		context['top_topic_list'] = top_topics
		return context

def search(request):
	query = request.GET.get("query")
	order_by = request.GET.get("order_by")
	n = NaverNews(query)
	n.fetch_articles()
	n.sort_by_time(order_by)
	top3_dict = n.plot_time_trend()
	context = { 'article_list': n.article_list,
				'top3_dict': top3_dict,
	}

	return render(request, 'news/search.html', context)