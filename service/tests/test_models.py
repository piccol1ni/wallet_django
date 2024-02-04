from django.test import TestCase
from django.contrib.auth.models import User
from wallet_manager.models import Wallet, Transaction

class WalletModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_wallet_creation(self):
        wallet = Wallet.objects.create(user=self.user, currency='USD', amount=100.0)
        self.assertEqual(wallet.user, self.user)
        self.assertEqual(wallet.currency, 'USD')
        self.assertEqual(wallet.amount, 100.0)

class TransactionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.wallet_from = Wallet.objects.create(user=self.user, currency='USD', amount=100.0)
        self.wallet_to = Wallet.objects.create(user=self.user, currency='RUB', amount=50.0)

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(wallet_from=self.wallet_from, wallet_to=self.wallet_to, amount=25.0)
        self.assertEqual(transaction.wallet_from, self.wallet_from)
        self.assertEqual(transaction.wallet_to, self.wallet_to)
        self.assertEqual(transaction.amount, 25.0)