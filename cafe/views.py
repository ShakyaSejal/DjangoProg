from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404 , get_object_or_404 ,redirect
from .models import Recipe, RecipeIngredients
from django import forms
from .forms import RecipeForm , RecipeIngredientsForm
from django.forms.models import modelform_factory



# Create your views here.
@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user = request.user)
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
    obj = get_object_or_404(Recipe, id = None)
    form = RecipeForm(request.POST or None, instance = obj)
    # form_2 = RecipeIngredientsForm(request.POST or None)
    RecipeIngredientsFormSet = modelform_factory(RecipeIngredients, form=RecipeIngredientsForm,extra=0)

    # ingredients_forms = []
    qs = obj.recipeingredients_set.all()
    # for ingredients_obj in obj.recipeingredients_set.all():
      
    #   ingredients_forms.append(RecipeIngredientsForm(request.POST or None))
    formset= RecipeIngredientsFormSet(request.POST or None, queryset=qs)
    context={
        "form":form,
        "formset": formset,
        "object":obj
    }
    if all([form.is_valid(), formset.is_valid()]):
        # form.save(commit=False)
        # form_2.save(commit = False)
        # print =("form", form.cleaned_data)
        # context["message"] = "Recipe has been successfully updated!!!"
       parent = form.save(commit=False)
       parent.save()
    for form in formset:
        child = form.save(commit=False)
        if child.recipe is None:
            print("added new")
            child.recipe =  parent
        child.save()            

        
        return render(request,"cafe/create_update.html",context)
