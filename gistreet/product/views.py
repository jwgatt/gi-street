from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ProductSerializer, CatagorySerializer
from .models import Product, Catagory


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, catagory_slug, product_slug,):
        try:
            return Product.objects.filter(catagory__slug=catagory_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, catagory_slug, product_slug, format=None):
        product = self.get_object(catagory_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CatagoryDetail(APIView):
    def get_object(self, catagory_slug):
        try:
            return Catagory.objects.get(slug=catagory_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, catagory_slug, format=None):
        catagory = self.get_object(catagory_slug)
        serializer = CatagorySerializer(catagory)
        return Response(serializer.data)
