from django.urls import path, include
from flanes import views

urlpatterns = [
    path('about_flans/', views.about_flans, name="about_flans"),
    path('welcome_flans/', views.welcome_flans, name="welcome_flans"),
    path('contact_flans/', views.contact_flans, name="contact_flans"),
    path('success_flans/', views.success_flans, name="success_flans"),
    path('index_flans/', views.index_flans, name="index_flans"),
    path('accounts_flans/', include("django.contrib.auth.urls")),
    path('flan/<int:flan_id>',views.flan_detail, name="flan_detail"),
    path('add_to_cart/<int:flan_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]