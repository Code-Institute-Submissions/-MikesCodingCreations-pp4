from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category, Comment
from django.http import HttpResponse
from taggit.models import Tag
from .forms import CommentForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list' : post_list,
    }

    return render(request, 'Post/post_list.html', context)

def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post_detail)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()
        else:
            comment_form = CommentForm()

    context = {
        'post_detail': post_detail,
        'categories': categories,
        'all_tags': all_tags,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'Post/post_detail.html', context)

def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__category_name=category)
    context = {
        'post_list': post_by_category,
    }

    return render(request, 'Post/post_list.html', context)


@login_required
def delete_post(request, id):
    """ Delete a blog post """

    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, f'Successfully deleted post "{post.title}".')

    context = {
        'post_list' : post_list,
    }

    return redirect('blog:post_list')


@login_required
def add_post(request):
    """ Add a Blog post """
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can access this.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect('blog:post_list')
        else:
            messages.error(request, 'Failed to add menu item.')
    else: form = BlogForm()

    template = 'Post/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
