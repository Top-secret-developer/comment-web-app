from django.shortcuts import render
from .forms import CommentForm
from .models import Post



# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
    

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            
    else:
        form = CommentForm()


    return render(request, 'detail.html', {'post' :post, 'form' :form} )
