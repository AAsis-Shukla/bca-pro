from django.urls import path
from primary import views

urlpatterns = [
    path('',views.index, name="index"),
    path('signup',views.signUp,name="signup"),
    path('login',views.user_login,name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('IoIndex',views.IoIndex,name="IoIndex"),
    path('deleteEntry/<id>',views.deleteEntry,name='deleteEntry'),
    path('IoUpdate/<id>',views.IoUpdate,name='IoUpdate'),
]