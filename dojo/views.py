# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import redirect, render

from dojo.forms import PostForm
from dojo.models import Post


def post_news(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'],
                        content = form.cleaned_data['content'])
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {'form':form,})



def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}씨. {}살이시네요.'.format(name, age))
