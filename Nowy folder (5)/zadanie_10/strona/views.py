from django.shortcuts import render, redirect
from .forms import AuthorForms, QuateForms
from .models import Author, Quate
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
    author=Author.objects.all()
    quate=Quate.objects.all()
    return render(request, 'strona/index.html', {"author":author})


@login_required
def author(request):
    if request.method=='POST':
        form= AuthorForms(request.POST)
        quate_form=QuateForms(request.POST)
        if form.is_valid() and quate_form.is_valid():
            author_instance = form.save()
            quate_instance = quate_form.save(commit=False)
            quate_instance.author = author_instance
            quate_instance.save()
            return redirect(to='strona:main')
        else:
            return render(request,'strona/author.html', { 'form': form,'quate_form': quate_form})
    return render(request,'strona/author.html', { 'form': AuthorForms(),'quate_form': QuateForms()})

