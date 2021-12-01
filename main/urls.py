from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.SearchRecipe.as_view(), name='search'),
    path('add_to_db/<int:id>/', views.FetchDataToDB.as_view(), name='add_to_db')
]