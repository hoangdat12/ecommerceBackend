from os import stat
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProductSerializers, CategorySerializers
from .models import Product, Category


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getProduct(request, pk):
    try:
        product = Product.objects.get(id = pk)
    except:
        return Response({'error' : 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializers(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error':'Create product is failure !'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def deleteProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({'detail': 'Delete product is successfully !'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getCategory(request):
    categorys = Category.objects.all()
    serializer = CategorySerializers(categorys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getProductCategory(request, pk):
    products = Product.objects.filter(category= pk)
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

