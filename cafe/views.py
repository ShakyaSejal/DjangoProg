from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404 , get_object_or_404 ,redirect
from .models import Recipe, RecipeIngredients
from django import forms
from .forms import RecipeForm , RecipeIngredientForm



# Create your views here.
@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(User = request.user)
    context={
        "object_list":qs
    }
    return render(request,"cafe/list.html", context)

@login_required
def recipe_detail_view(request, id = None):
    obj = get_list_or_404(Recipe, id=id , user=request.user)
    context={
        "object":obj
    }

    return render(request, "cafe/detail.html", context)


@login_required
def recipe_create_view(request):## create -> list
    form = RecipeForm(request.POST or None)
    context ={
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit= False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "cafe/create-update.html", context)


@login_required
def recipe_update_view(request):
    obj = get_object_or_404(Recipe, id = id, user=request.user)
    form = RecipeForm(request.POST or None, instance = obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    ingredients_forms = []
    for ingredients_obj in obj.recipeingredients_set.all():
      
      ingredients_forms.append(RecipeIngredientForm(request.POST or None))
    context={
        "form":form,
        "form_2": form_2,
        "ingredients_forms": ingredients_forms,
        "object":obj
    }
    if all([form.is_valid(), form_2.is_valid()]):
        form.save(commit=False)
        form_2.save(commit = False)
        print =("form", form.cleaned_data)
        context["message"] = "Recipe has been successfully updated!!!"
    
        
        return render(request,"cafe/create_update.html",context)
