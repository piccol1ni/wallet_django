import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer

logger = logging.getLogger(__name__)

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        wallet_from_id = request.data.get('wallet_from')
        wallet_to_id = request.data.get('wallet_to')
        amount = float(request.data.get('amount'))

        wallet_from = Wallet.objects.get(id=wallet_from_id)
        wallet_to = Wallet.objects.get(id=wallet_to_id)

        if wallet_from.currency == wallet_to.currency:
            if wallet_from.amount >= amount:
                wallet_from.amount -= amount
                wallet_from.save()

                wallet_to.amount += amount
                wallet_to.save()

                transaction = Transaction.objects.create(wallet_from=wallet_from, wallet_to=wallet_to, amount=amount)
                serializer = TransactionSerializer(transaction)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.warning("Insufficient funds")
                return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.warning("Invalid currency: %s != %s", wallet_from.currency, wallet_to.currency)
            return Response({'error': 'Currency not valid'}, status=status.HTTP_400_BAD_REQUEST)
