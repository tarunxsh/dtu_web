from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request,'index.html',{'posts':posts})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def newpost(request):
	if request.method == 'POST':
		print(request.POST)
		title = request.POST['title']
		descp = request.POST['descp']
		author = request.user
		post = Post.objects.create(title=title,descp=descp,author=author)
		return redirect('post_detail',pk=post.pk) 

	else:	
		return render(request,'newpost.html')    


def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	
	
	#print(type(post.author))
	author = post.author
	#print(type(author))
	#print(type(request.user))
	return render(request,'post_detail.html', {'post':post})


def post_publish(request, pk):
	post = Post.objects.get(pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)



def post_draft_list(request):
	author = request.user
	posts = Post.objects.filter(published_date__isnull=True,author=author).order_by('-created_date')
	return render(request,'post_draft_list.html', {'posts':posts})
	



def post_remove(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')


def post_edit(request,pk):
	post = Post.objects.get(pk=pk)
	
	if request.method == 'POST':
		edited_title = request.POST['edited_title']
		edited_descp =request.POST['edited_descp']
		print(edited_title,edited_descp)
		Post.objects.filter(pk=pk).update(title=edited_title,descp=edited_descp)
		post_publish(request,pk)
		return redirect('post_detail',pk=pk)

		


	else:
		return render(request,'post_edit.html',{'post':post})	
