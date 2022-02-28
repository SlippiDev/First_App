from django import forms
from .models import contactform1
class StudentFormUpload(forms.Form):
    firstname = forms.CharField(label = 'Enter First Name', max_length=50)
    lastname = forms.CharField(label = 'Enter Last Name', max_length=50)
    file = forms.FileField()
class formcontactform(forms.ModelForm):
    class Meta:
        model = contactform1
        fields = ["fullname", "email", "contact", "message"]

        
