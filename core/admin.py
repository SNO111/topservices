from django.contrib import admin
from django.utils import tree
from .models import Item, OrderItem, Order, Payment, Coupon, Refound, Address

# Register your models here.


def make_refound_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refound_granted=True)


make_refound_accepted.short_description = 'Upfate order to refound granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refound_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon']

    list_display_links = ['user',
                          'shipping_address',
                          'billing_address',
                          'payment',
                          'coupon']

    list_filter = ['being_delivered',
                   'received',
                   'refund_requested',
                   'refound_granted']

    search_fields = ['user__username', 'ref_code']

    actions = [make_refound_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'streat_address',
                    'apartment_address',
                    'country',
                    'city',
                    'zip',
                    'address_type',
                    'default']

    list_filter = ['country',
                   'city',
                   'address_type',
                   'default']
    search_fields = ['user',
                     'streat_address',
                     'apartment_address',
                     'zip']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refound)
admin.site.register(Address, AddressAdmin)
