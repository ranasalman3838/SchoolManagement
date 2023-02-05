from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('backend/',views.backend,name="backend")
    # path('frontend/',views.frontend,name="frontend"),
]