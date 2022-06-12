from rest_framework import serializers
from .models import Crypto


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ["id", 'crypto_id', 'buying_price', 'quantity', 'notes']