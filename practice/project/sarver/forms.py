from django import forms

#Creating a form
class user(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.IntegerField(widget=forms.PasswordInput)
    def clean_password(self):
       password_valid = self.cleaned_data['password']
       if len(password_valid)<4:
        raise forms.ValidationError('eror 044')
       return password_valid 
    



 








