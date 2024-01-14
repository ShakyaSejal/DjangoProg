from django.urls import path
from .views import recipe_create_view, recipe_detail_view, recipe_update_view, recipe_list_view



app_name = "cafe"
urlpatterns = [
      path("",recipe_list_view, name="list"), ##list view
      path("create/",recipe_create_view, name="create"),
      path("<int:id>/update/",recipe_update_view, name="update"),
      path("<int:id>/detail/",recipe_update_view, name="detail"),




]