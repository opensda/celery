from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

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
