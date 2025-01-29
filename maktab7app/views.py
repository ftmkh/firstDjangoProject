from django.shortcuts import render,redirect , get_object_or_404
from comments.forms import CommentForm
from comments.models import Comments
from django.contrib import messages
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


'''def single_blog(request,title):
    post = get_object_or_404(Post,title=title,status=1)
    comments = post.comments.all()
    form = CommentForm()
    #return render(request, 'maktab7app/single_blog.html', {'post': post})
    if request.method == "POST":
        form = CommentForm(request.POST)
        if not post.login_require:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
        else:
            return redirect('accounts/login')
    return render(request,'maktab7app/single_blog.html', {
    'post': post,
    'comments': comments,
    'form': form,
    })'''


def single_blog(request,post_title):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'successfully')
        else:
            messages.add_message(request,messages.SUCCESS,'not success')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,title=post_title)
    if not post.login_require :
        comments = Comments.objects.filter(post=post.id,approved=True)
        form=CommentForm()
        context ={'post':post , 'comments':comments , 'form':form}
        return render(request,'maktab7app/single_blog.html',context)
    else:
        return redirect('accounts/login.html')