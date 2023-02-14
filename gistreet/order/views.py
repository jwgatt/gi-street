import stripe

from django.http import JsonResponse
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


def orders_list(request):
    orders = Order.objects.all()
    order_data = [{'id': order.id, 'description': order.description}
                  for order in orders]
    return JsonResponse({'orders': order_data})


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum([item['quantity']*item['product']['price']
                          for item in request.data['items']])

        try:
            charge = stripe.Charge.create(
                amount=max(int(paid_amount * 100), 100),
                currency='usd',
                source=serializer.validated_data['stripe_token'],
                description='Charge from Gistreet'
            )
            order = serializer.save()
            order.user = request.user
            order.save()

            for item in request.data['items']:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity']
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


def current_user(request):
    user = request.user
    if user.is_authenticated:
        return JsonResponse({
            'username': user.username, })
    else:
        return JsonResponse({})
