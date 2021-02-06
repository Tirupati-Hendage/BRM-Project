from django import forms
from .models import Book
class NewBookForm(forms.Form):
    id = forms.IntegerField(label='Id')
    title = forms.CharField(label = 'Title', max_length=100)
    price = forms.FloatField(label = 'Price')
    author = forms.CharField(label = 'Author')
    publisher = forms.CharField(label = 'Publisher')


#class NewBookForm(forms.ModelForm):
#    class Meta:
#        model = Book
#        fields = '__all__' #(optional)
#        fields = ['title', 'price', 'author', 'publisher']


class SearchForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length=100)
