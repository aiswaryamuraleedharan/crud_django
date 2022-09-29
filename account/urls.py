from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('update/<str:pk>',views.Update,name='update'),
    path('delete/<str:pk>',views.DeleteUser,name='delete')
]
