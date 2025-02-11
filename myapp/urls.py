from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('travellers/', views.travellers, name="travellers"),
    path('about/', views.about, name="about"),
    path('savecabdata/', views.saveCabdata, name="savecabdata"),
    path('contact/', views.contact, name="contact"),
    path('contact/submitdataContact', views.submitdataContact, name="submitdataContact"),
    path('reservation/', views.reservation, name="reservation"),
    path('reservation/submitdataResrvation', views.submitdataResrvation, name="submitdataResrvation"),
    path('home2/', views.home2, name="home2"),
    path('directions.html/cars2.html', views.cars2, name="cars2"),
    path('directions.html/cars3.html/', views.cars3, name="cars3"),
    path('directions.html/cars4.html/', views.cars4, name="cars4"),
    path('directions.html/cars5.html/', views.cars5, name="cars5"),
    path('directions.html/cars6.html/', views.cars6, name="cars6"),
    path('directions.html/cars7.html/', views.cars7, name="cars7"),
    path('travellers/directions.html/cars2.html', views.cars2, name="cars2"),
    path('travellers/directions.html/cars3.html/', views.cars3, name="cars3"),
    path('travellers/directions.html/cars4.html/', views.cars4, name="cars4"),
    path('travellers/directions.html/cars5.html/', views.cars5, name="cars5"),
    path('travellers/directions.html/cars6.html/', views.cars6, name="cars6"),
    path('travellers/directions.html/cars7.html/', views.cars7, name="cars7"),
    path('p0000p-up/', views.popup1, name="popup1"),
    path('page1/', views.page1, name="page1"),
    path('success/', views.payment_success, name='payment_success'),
    path('pay/', views.payment_page, name='payment_page'),
    path('pay/',views.booking_view, name="booking_view"),
    path('<my_id>/', views.directions, name="directions"),
    path('travellers/<my_id2>/', views.direction2, name="direction2"),
    path('verify_payment',views.verify_payment,name='verify_payment'),
    path('submitdata', views.submitdata, name="submitdata"),
    path('submitdata2', views.submitdata2, name="submitdata2"),
    path('Tour/', views.Tour, name="Tour"),
    path('home/popular/<int:drop_id>', views.popular, name="popular"),
    path('home/popularCity/<int:drop_id>', views.popularCity, name="popularCity"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)