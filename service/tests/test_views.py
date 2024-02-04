from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from wallet_manager.models import Wallet, Transaction

class WalletViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.wallet = Wallet.objects.create(user=self.user, currency='USD', amount=100.0)

    def tearDown(self):
        Wallet.objects.all().delete()

    def test_get_wallets(self):
        url = '/api/wallets/'
        response = self.client.get(url)
        results = response.data.get('results', [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['user'], self.user.id)
        self.assertEqual(results[0]['currency'], 'USD')
        self.assertEqual(results[0]['amount'], 100.0)

class TransactionViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.wallet_from = Wallet.objects.create(user=self.user, currency='USD', amount=100.0)
        self.wallet_to = Wallet.objects.create(user=self.user, currency='RUB', amount=50.0)
        self.transaction = Transaction.objects.create(wallet_from=self.wallet_from, wallet_to=self.wallet_to, amount=25.0)

    def tearDown(self):
        Wallet.objects.all().delete()
        Transaction.objects.all().delete()

    def test_get_transactions(self):
        url = '/api/transactions/'
        response = self.client.get(url)
        results = response.data.get('results', [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['wallet_from'], self.wallet_from.id)
        self.assertEqual(results[0]['wallet_to'], self.wallet_to.id)
        self.assertEqual(results[0]['amount'], 25.0)