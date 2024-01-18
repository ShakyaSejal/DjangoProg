"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view
from student import views
from accounts.views import login_views, logout_views ,register_views
from student.views import detail_view
from cafe import views
from cafe.views import recipe_create_view,recipe_detail_view,recipe_update_view
from django.urls import include



urlpatterns = [
   #   path("", home_view, name="home"),
    #    path("recipe/create/",views.receipe_create_view, name="recipe_create"),
    #   path("recipe/<int:id>/",views.receipe_detail_view, name="recipe_detail"),
    #   path("recipe/<int:id>/update/",views.receipe_update_view, name="recipe_update"),
      path("cafe/", include("cafe.urls")),
    #   path("students/details", views.detail_view),
    #   path("students/<int:id>", views.student_view),
      path('admin/', admin.site.urls),
      path('login/',login_views),
      path('logout/',logout_views),
      path('register/',register_views),
    
]
    

