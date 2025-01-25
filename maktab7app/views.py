from django.shortcuts import render,redirect , get_object_or_404
from comments.forms import CommentForm
from .models import Post

def home(request):
    return render(request,'maktab7app/index.html')

#def blog(request):
#    return render(request,'maktab7app/blog.html')


def bolgs(request,author=None):
    if author != None:
        posts = Post.objects.filter(author=author , status=1)
    else:
        posts = Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'maktab7app/blog.html',context)


def single_blog(request,title):
    post = get_object_or_404(Post,title=title,status=1)
    comments = post.comments.all()
    form = CommentForm()
    #return render(request, 'maktab7app/single_blog.html', {'post': post})
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return render(request,'maktab7app/single_blog.html', {
    'post': post,
    'comments': comments,
    'form': form,
    })