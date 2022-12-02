from django import forms

class FormTios(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    proveniente=forms.CharField(max_length=10)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class FormHermanos(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()
