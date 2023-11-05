from rest_framework import generics

from education.models import Subscription
from education.serializers.subscription import (
    SubscriptionListSerializer,
    SubscriptionSerializer,
    SubscriptionDetailSerializer,
)


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionListSerializer
    queryset = Subscription.objects.all()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscriptionDetailSerializer
    queryset = Subscription.objects.all()


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
