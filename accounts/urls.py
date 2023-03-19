from django.urls import path
from . import views


urlpatterns = [
    path('', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('index/', views.index, name="index"),
    path('index/contact/', views.contact, name="contact"),
    path('index/rooms_list/', views.rooms_list, name='rooms_list'),
    path('index/booking_list/', views.booking_list, name='booking_list'),
    path('index/book/', views.book, name="book"),
    path('index/book/user_book/', views.user_book, name="user_book"),
    path('index/home/', views.HomepageView),
    path('index/home/', views.contactView),
    path('index/home/', views.roomView),
    path('index/home/', views.bookView)

]
