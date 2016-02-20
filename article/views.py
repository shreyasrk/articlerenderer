from django.http import HttpResponse

from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.order_by('-publ_date')[:5]
    return HttpResponse(article_list)

