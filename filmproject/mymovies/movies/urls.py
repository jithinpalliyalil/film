from django.urls import path
from.import views
app_name='movies'
urlpatterns = [

    path('',views.index,name='index'),
    path('movielist/<int:movieid>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add',views.add,name='add'),
]