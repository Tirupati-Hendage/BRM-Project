from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import NewBookForm, SearchForm
from .models import Book
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def UserLogin(request):
    data = {}
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(request, username=uname, password=upass)
        if user:
            login(request, user)
            request.session['username'] = uname
            return HttpResponseRedirect('/BRM/view-book/')
        else:
            data['error'] = 'username or password is incorrect'
            return render(request, 'myapp/user_login.html', data)
    else:
        return render(request, 'myapp/user_login.html', data)


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRM/login/')


@login_required(login_url = '/BRM/login/')
def ViewBooks(request):
    books = Book.objects.all().order_by('id')
    username = request.session['username']
    context = {
        'books' : books,
        'username' : username
    }
    return render(request, 'myapp/view_book.html',context)


@login_required(login_url = '/BRM/login/')
def NewBook(request):
    username = request.session['username']
    if request.method == 'POST':
        fm = NewBookForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            price = fm.cleaned_data['price']
            author = fm.cleaned_data['author']
            publisher = fm.cleaned_data['publisher']
            user = Book(title=title, price=price, author=author, publisher=publisher)
            user.save()
            return HttpResponseRedirect('/BRM/view-book/')
    else:
        fm = NewBookForm()
    context = {
        'form' : fm,
        'username' : username
        }
    return render(request, 'myapp/new_book.html', context)


@login_required(login_url = '/BRM/login/')
def EditBook(request, id=None):
    username = request.session['username']
    if request.method == 'POST':
        pi = get_object_or_404(Book, pk=id)
        fm = NewBookForm(request.POST or None)
        print(fm)
        if fm.is_valid():
#            id = fm.cleaned_data['id']
            title = fm.cleaned_data['title']
            price = fm.cleaned_data['price']
            author = fm.cleaned_data['author']
            publisher = fm.cleaned_data['publisher']
            obj = Book(title=title, price=price, author=author, publisher=publisher)
            obj.save()
            messages.success(request, 'You successfully updated the Book')
            return HttpResponseRedirect('/BRM/view-book/')
        else:
            messages.warning(request, 'Pls enter a valid data!!')
    else:
        pi = get_object_or_404(Book, pk=id)
        book = {'title' : pi.title, 'price' : pi.price, 'author' : pi.author, 'publisher' : pi.publisher}
        fm = NewBookForm(initial=book)
    context = {
        'form' : fm,
        'username' : username
    }
    return render(request, 'myapp/edit_book.html', context)



@login_required(login_url = '/BRM/login/')
def DeleteBook(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect('/BRM/view-book/')




@login_required(login_url = '/BRM/login/')
def SearchBook(request):
    username = request.session['username']
    if request.method == 'GET':
        fm = SearchForm()
        books = None
    elif request.method == 'POST':
        fm = SearchForm(request.POST)
        books = Book.objects.filter(title__icontains = fm.data['title'])
    context = {
        'form' : fm,
        'books' : books,
        'username' : username
    }
    return render(request, 'myapp/search_book.html',context)
