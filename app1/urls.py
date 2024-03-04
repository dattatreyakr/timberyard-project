from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('order/',views.orderRequest,name="order"),
    path('conform/',views.confirmOrder,name="conform"),
    path('loginpage/',views.loginPage,name="log"),
    path('signupPage/',views.signupPage,name="sign"),
    path('profile/',views.profile,name="profile"),
    path('pay/',views.payment_complete,name="pay"),
    path('payd/',views.payd,name="payd")
]
