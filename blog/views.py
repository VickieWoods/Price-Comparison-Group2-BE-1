from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product, Comment
from blog.models import Comment
#from django.shortcuts import render, get_object_or_404



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'created_date')

# IMPLEMENT THE COMMENT VIEWS HERE. THANKS

def comment_add(request):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = comment_add
            #comment.post = post

            comment.save()
            return redirect('post_detail')
           
    else:
        form = CommentForm()
    return render(request, 'comments/comment.html', {'form': form})
    
