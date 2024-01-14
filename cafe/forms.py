from django import forms
from .models import Recipe , RecipeIngredients

class RecipeForm(forms.ModelForm):
    class Meta:
        model =  Recipe
        fields = [
            'name',
            'description',
            'direction',
        ]
class RecipeIngredients(forms.Form):
  
        model =  RecipeIngredients
        fields = [
            'name',
            'quantity',
            'unit',
        
        ]

