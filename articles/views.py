from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Book


def article_list(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(title__icontains=query) | \
                   Article.objects.filter(content__icontains=query)
    else:
        articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'query': query,
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    article.views += 1
    article.save(update_fields=['views'])

    tag_ids = article.tags.values_list('id', flat=True)
    similar = Article.objects.filter(tags__id__in=tag_ids).exclude(id=article.id).distinct()[:3]

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'similar': similar,
    })


def book_list(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query) | \
                Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'articles/book_list.html', {
        'books': books,
        'query': query,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'articles/book_detail.html', {'book': book})