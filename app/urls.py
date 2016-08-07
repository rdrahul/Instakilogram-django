from django.conf.urls import url
from . import views
urlpatterns=(
    url(r'^items/$',views.view_items,name='item_list'),
    url(r'^items/(?P<id>\d+)$',views.item_detail,name='item_detail'),
    url(r'^items/(?P<id>\d+)$',views.photo_detail,name='photo_detail'),
    url(r'^createalbum/$',views.create_album,name='create_album'),
    url(r'^photos/(?P<id>\d+)/addphoto/$',views.add_photo,name='add_photo'),
    url(r'^delete/(?P<id>\d+)/$',views.delete_album,name='del_album')
)
