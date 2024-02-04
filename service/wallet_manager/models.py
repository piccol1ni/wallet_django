from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Wallet(models.Model):
    CURRENCY_CHOICES = [
        ('RUB', 'RUB'),
        ('USD', 'USD')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(choices=CURRENCY_CHOICES)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user} : {self.currency} wallet №{self.pk}'

class Transaction(models.Model):
    wallet_from = models.ForeignKey(Wallet, related_name='sent_transaction', on_delete=models.CASCADE)
    wallet_to = models.ForeignKey(Wallet, related_name='receive_transaction', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.wallet_from.currency != self.wallet_to.currency:
            raise ValidationError("Transfers can only be made between wallets with the same currency.")

    def __str__(self):
        return f'{self.wallet_from} to {self.wallet_to} : {self.amount}'