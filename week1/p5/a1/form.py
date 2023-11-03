from django import forms

class Student(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean_name(self):
      valname = self.cleaned_data['name']
      if len(valname)<10:
        print("indeside")
        raise forms.ValidationError("name must be at least 10 char")
      return valname
    

# widgets = field to heml input
class contact_form(forms.Form):
    name = forms.CharField(label="user name",help_text="must be in 70"
      ,required=False,disabled=True  ,widget=forms.Textarea (attrs={'id':'text','placeholder':'enter your name'})          )
    email = forms.EmailField(label="user email")
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    bllence = forms.DecimalField()
    check = forms.BooleanField()
    bithday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    choices = [('s',"small"),('m',"medium"),('l',"large")]
    size = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    
    meal =  [('s',"sosa"),('m',"moriz"),('l',"lebu")]
    food = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    #file  = forms.FileField()
    