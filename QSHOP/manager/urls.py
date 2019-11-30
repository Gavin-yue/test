from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('check_username/',views.check_username,name = "check_username"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('add_goods/',views.add_goods,name="add_goods"),

]

app_name = 'manager'