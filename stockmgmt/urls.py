from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('list_items/', views.list_items, name='list_items'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    # path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    # path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    #path('SaveCart',views.saveCart,name ='saveCart'),
]
