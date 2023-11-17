
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('picture/<int:photo_id>', views.picture_detail, name='picture_detail'),
    path('addpost', views.add_post, name='add_post'),

]

