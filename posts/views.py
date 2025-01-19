from django.shortcuts import render, get_object_or_404
from .models import Post
from catalogs.models import Category
from authors.models import Author
from tags.models import Tag


def home(request):
    posts = Post.objects.all()
    catalogs = Category.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    category_id = request.GET.get('category')
    author_id = request.GET.get('author')
    tag_id = request.GET.get('tag')
    if category_id:
        posts = posts.filter(category__id=category_id)
    if author_id:
        posts = posts.filter(author__id=author_id)
    if tag_id:
        posts = posts.filter(tags__id=tag_id)
    ctx = {
        'posts':posts,
        'catalogs':catalogs,
        'authors':authors,
        'tags':tags
    }
    return render(request, 'index_with_side_bar.html', ctx)

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug = slug,
        posted_at__year = year,
        posted_at__month = month,
        posted_at__day = day
    )
    ctx = {'post':post}
    return render(request, 'posts/post-detail.html', ctx)