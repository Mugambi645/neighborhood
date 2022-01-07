
from django.urls import path,include,re_path
from . import views
app_name = "blog"
urlpatterns = [
    path("blogs", views.blogs, name="blogs"),
    path("add_blogs", views.add_blogs, name="add_blogs"),
]