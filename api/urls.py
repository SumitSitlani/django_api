from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview),
    path('user-list/',views.userList),
    path('user-detail/<str:pk>/',views.userDetail),
    path('user-create/',views.userCreate),
    path('user-update/<str:pk>/',views.userUpdate),
    path('user-delete/<str:pk>/',views.userDelete),

]