from rest_framework.relations import SlugRelatedField

from education.models import Subscription, Course
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionListSerializer(serializers.ModelSerializer):
    # Меняем id курса на его название

    course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())

    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
