from django import forms
from catagory.models import Catagory
from book.models import Book
class BookForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    description = forms.CharField()
    version = forms.IntegerField()
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    publish_date = forms.DateField()
    catagory = forms.ChoiceField(choices=[(cat.id,cat.name) for cat in Catagory.objects.all()])

class BookFormModel(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

    def validate_age(self,values):
        pass