from django import forms
from .models import Recipe , RecipeIngredients

class RecipeForm(forms.ModelForm):
    class Meta:
        model =  Recipe
        fields = [
            'name',
            'description',
            'directions',
        ]
class RecipeIngredientsForm(forms.Form):
  
        model =  RecipeIngredients
        fields = [
            'name',
            'quantity',
            'unit',
        
        ]

