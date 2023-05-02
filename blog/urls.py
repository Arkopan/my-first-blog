from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    #path("",views.post_list,name='post_list'),
    #path("post/<int:pk>/",views.post_detail,name='post_detail'),
    #path("post/new/",views.post_new,name="post_new"),
    #path("post/<int:pk>/edit/>",views.post_edit,name="post_edit"),
    path('', views.post_published, name='post_published'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail')
    ]