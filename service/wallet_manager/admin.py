from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Wallet, Transaction
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

class WalletInline(admin.StackedInline):
    model = Wallet
    extra = 0

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1
    fk_name = 'wallet_from'

class CustomUserAdmin(UserAdmin):
    inlines = [WalletInline]

    def wallet_balance(self, obj):
        wallets = Wallet.objects.filter(user=obj)
        balance = sum(wallet.amount for wallet in wallets)
        return balance

    wallet_balance.short_description = 'Total Wallet Balance'

    def wallet_link(self, obj):
        wallets = Wallet.objects.filter(user=obj)
        if wallets.exists():
            wallet_id = wallets.first().id
            url = reverse('admin:wallet_manager_wallet_change', args=[wallet_id])
            return format_html('<a href="{}">View Wallet</a>', url)
        return '-'

    wallet_link.short_description = 'Wallet Card'

    list_display = UserAdmin.list_display + ('wallet_balance', 'wallet_link')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet_from', 'wallet_to', 'amount', 'timestamp')
    search_fields = ('wallet_from__user__username', 'wallet_to__user__username')

class WalletAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ('user', 'currency', 'amount', 'transaction_history_link')
    search_fields = ('user__username', 'currency')

    def transaction_history_link(self, obj):
        url = reverse('admin:wallet_manager_transaction_changelist') + f'?wallet_from__id__exact={obj.id}'
        return format_html('<a href="{}">View Transactions</a>', url)

    transaction_history_link.short_description = 'Transaction History'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
