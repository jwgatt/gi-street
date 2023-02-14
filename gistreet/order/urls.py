from django.urls import path

from order import views
from order.views import OrderListView

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path('current_user/', views.current_user, ),
    path('api/v1/orders/', OrderListView.as_view(), name='order-list'),
]
