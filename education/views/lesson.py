from rest_framework import generics

from education.models import Lesson
from education.paginators import LessonPaginator
from education.serializers.lesson import (
    LessonListSerializer,
    LessonDetailSerializer,
    LessonSerializer,
)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
