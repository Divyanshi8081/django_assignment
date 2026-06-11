from django.urls import path
from . import views

urlpatterns = [
    path('register/',    views.register_view,    name='register'),
    path('login/',       views.login_view,        name='login'),
    path('logout/',      views.logout_view,       name='logout'),
    path('create-post/', views.create_post_view,  name='create_post'),
]
