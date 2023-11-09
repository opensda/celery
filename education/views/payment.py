import os

from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

import stripe

from education.models import Payment
from education.serializers.payment import PaymentListSerializer, PaymentDetailSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "course",
        "lesson",
        "payment_choice",
    )
    ordering_fields = ("date",)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()




stripe.api_key = os.getenv('STRIPE_API_KEY')


# Создаем продукт

starter_subscription = stripe.Product.create(
  name="Курс Python - разработчик 99.0",
  description="Оплата за 10 месяцев",
)

# Создаем цену

starter_subscription_price = stripe.Price.create(
  unit_amount=1200,
  currency="usd",
  recurring={"interval": "month"},
  product=starter_subscription['id'],
)


# Создаем ссылку


stripe.PaymentLink.create(line_items=[{"price": starter_subscription_price.id, "quantity": 1}])


