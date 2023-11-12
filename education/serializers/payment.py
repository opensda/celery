from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Payment
from users.models import User


class PaymentListSerializer(serializers.ModelSerializer):
    # Меняем id курса на его название

    # course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())

    # Меняем id пользователя на его почту

    # user = SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentDetailSerializer(serializers.ModelSerializer):
    # course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())
    # user = SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
