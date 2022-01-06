from django.urls import path
from .views import PostCreateView
from . import views
app_name = "homepage"
urlpatterns = [
    path("",views.index, name="index"),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
]