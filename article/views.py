from django.http import HttpResponse

from .models import Article


def index(request):
    article_list = Article.objects.order_by('-publ_date')[:5]
    response = HttpResponse(article_list, content_type='application/jpeg')
    response['Content-Disposition'] = 'attachment; filename="foo.jpg"'
    return response
