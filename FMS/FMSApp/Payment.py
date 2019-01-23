from decimal import Decimal

from payments import get_payment_model

Payment = get_payment_model()
payment = Payment.objects.create(
    variant='default',  # this is the variant from PAYMENT_VARIANTS
    description='Book purchase',
    total=Decimal(10),
    tax=Decimal(10),
    currency='INR',
    delivery=Decimal(1),
    billing_first_name='Sherlock',
    billing_last_name='Holmes',
    billing_address_1='221B Baker Street',
    billing_address_2='',
    billing_city='London',
    billing_postcode='500073',
    billing_country_code='IN',
    billing_country_area='Greater London',
    customer_ip_address='122.175.53.53')
