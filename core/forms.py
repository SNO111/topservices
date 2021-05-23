from django import forms
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.forms.forms import Form
from django.shortcuts import redirect
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(required=False, widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100 ',
    }))
    shipping_city = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(required=False, widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100 ',
    }))
    billing_city = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code...',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'

    }))


class RefoundForm(forms.Form):
    ref_code = forms.CharField(label='Refound Code')
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'style': 'height:100%',
        'placeholder': 'What is the resson for your refound request?',
    }))


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
