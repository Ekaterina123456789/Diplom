from .models import Tag, Blog, Profiles
from django.db.models import Q


def search_blogs(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        # search_query = search_query.strip()

    tags = Tag.objects.filter(name__iexact=search_query)

    autor = Profiles.objects.filter(Q(name__icontains=search_query) |
                                    Q(username__icontains=search_query))

    blogs = Blog.objects.distinct().filter(Q(title__icontains=search_query) |
                                           Q(tags__in=tags) |
                                           Q(owner__in=autor))

    return blogs, search_query
