from django import forms
from .models import Book,Student ,Address,Student22,Address22,Profile


class BookForm(forms.ModelForm):  
    class Meta:
        model = Book
        fields = ['title', 'author','price','edition']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student22
        fields = '__all__'
        
class AddressForm2(forms.ModelForm):
    class Meta:
        model = Address22
        fields = '__all__'
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo']



