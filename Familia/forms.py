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

class FormPrimos(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class FormViven(forms.Form):
    ciudad=forms.CharField(max_length=50)
    estado=forms.CharField(max_length=50)

class FormTrabajan(forms.Form):
    profesion=forms.CharField(max_length=50)
    titulo=forms.CharField(max_length=30)
    mail=forms.EmailField()
    activo=forms.BooleanField()
