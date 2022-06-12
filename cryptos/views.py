from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404, HttpResponseForbidden, JsonResponse
from .models import Crypto
from .serializers import CryptoSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_get_cryptos(request):
    if request.method == "POST":
        new_crypto_data = request.data
        crypto_id = new_crypto_data['crypto_id']
        buying_price = new_crypto_data['buying_price']
        quantity = new_crypto_data['quantity']
        notes = new_crypto_data['notes']
        crypto = Crypto(
            crypto_id=crypto_id,
            buying_price=buying_price,
            quantity=quantity,
            notes=notes,
            user=request.user
            )
        crypto.save()

    cryptos = Crypto.objects.filter(user=request.user)

    serialized_cryptos = CryptoSerializer(cryptos, many=True)
    return Response(serialized_cryptos.data)

@api_view(['POST'])
def api_register(request):
    try:
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({"token": token.key})
    except:
        return HttpResponseForbidden()

