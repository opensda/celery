import os

from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

import stripe
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from education.models import Payment
from education.serializers.payment import (
    PaymentListSerializer,
    PaymentDetailSerializer,
    PaymentSerializer,
)


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


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Создает и обрабатывает платеж"""

        stripe.api_key = os.getenv("STRIPE_API_KEY")

        # Достаем id курса для оплаты

        course_id = request.data.get("course")

        # Создаем платежное намерение

        response = stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
        )

        # Подтверждаем платеж

        stripe.PaymentIntent.confirm(
            response.id,
            payment_method="pm_card_visa",
        )

        # Забираем данные о пользователе, который исполнил платеж

        user = self.request.user

        # Заносим данные о платеже в БД

        data = {"user": user.id, "course": course_id, "is_confirmed": True}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
