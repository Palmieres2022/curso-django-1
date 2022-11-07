from django.urls import path
from recipes import views  # posso usar . no lugar de recipes

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewBase.as_view(), name="home"),  # Home
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]