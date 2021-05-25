from django.urls import path

from .views import ReposList
    
app_name = 'carts'
urlpatterns = [
    path('get_repos/<str:username>', ReposList.as_view(), name='get_list_of_repos_of_an_user'),
    #path('checkout/', RepoDetail., name='checkout'),
    
]