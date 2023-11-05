from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson
from education.validators import video_link_validator
from users.models import NULLABLE


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[video_link_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonListSerializer(serializers.ModelSerializer):
    # Меняем id курса на его название

    course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
