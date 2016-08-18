from django.shortcuts import render
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__isnull = True).order_by('published_date')
	
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def hello_world(request):
	return render(request, 'blog/hello.html', {})
	
def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
