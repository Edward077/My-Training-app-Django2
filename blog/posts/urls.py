
from django.urls import path
from . import views

urlpatterns = [
    # path('helloworld/', views.helloword),
    # path('home/<str:name>/', views.home, name ='home'),
    path('home/', views.home),

    path("<int:ID>/", views.post, name='post'), # we alpply path converter int
]
