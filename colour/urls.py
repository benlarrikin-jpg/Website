from django.urls import path
from colour.views import food_view,food_list
 
urlpatterns = [
    path('burn/', food_view , name='room'),
    path('red/', food_list, name='text')
] 