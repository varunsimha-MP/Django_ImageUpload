from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexpage,name="index"),
    path("upload",views.UploadImage,name="imageupload"),
    path("show",views.ImageFetch,name="show"),
    path("back",views.Back,name="back")
]
