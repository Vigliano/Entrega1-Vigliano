from django import forms

class AutoFormulario(forms.Form):

    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    fabricacion = forms.IntegerField()
    kilometraje = forms.IntegerField()

class CamionetaFormulario(forms.Form):

    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    fabricacion = forms.IntegerField()
    kilometraje = forms.IntegerField()

class MotoFormulario(forms.Form):

    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    fabricacion = forms.IntegerField()
    kilometraje = forms.IntegerField()


