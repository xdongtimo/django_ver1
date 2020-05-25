from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all().order_by('-data')
    template_name = 'blogs/blog.html'
    context_object_name = 'Posts'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post.html'

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blogs/post.html", {"post": post, "form": form})