from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<slug:slug>/', views.postdetails, name='post_detail'),
    path('create', views.createpost, name='create')
]
