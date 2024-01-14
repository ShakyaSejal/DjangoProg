from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe
from .models import RecipeIngredients
from django.contrib.auth.models import user




# Create your tests here.

def test_user_pw(self):
    checked = self.user_a.password('password123')
    self.assertTrue(checked)

    class RecipeTestCase(TestCase):
        def setup(self):
            self.user_a = get_user_model().object.create_user(username = 'Sejal',password='123')
            self.recipe_a = Recipe.objects.create(
            name='pizza',
            user = self.user_a,
         )
            self.recipe_b= Recipe.objects.create(
            name='burger',
            user = self.user_b,
         )
            self.recipe_b= RecipeIngredients.objects.create(
            name='burger',
            user = self.user_b,
         )
        
        # def test_user_count(self):
        #     qs = user.objects.all()
        #     self.assertEqual(qs.count(),1)
        
        # def test_user_recipe_reverse_count(self):
        #     user = self.user_a()
        #     qs = user.recipe_set.all()
        #     self.assertEqual(qs.count(),1)

        def test_recipe_ingredients_reverse_count(self):
            recipe = self.recipe_b
            qs = recipe.recipe_ingredient_set.all()
            self.assertEqual(qs.count(),1)



    # class RecipeTestCase(TestCase):
    #     def setup(self):
     