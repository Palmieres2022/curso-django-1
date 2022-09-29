from django.urls import path
from recipes import views  # posso usar . no lugar de recipes

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # Home
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]