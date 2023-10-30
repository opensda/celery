from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from education.models import Course, Lesson, Payment
from education.serializers import LessonListSerializer, CourseDetailSerializer, \
    LessonDetailSerializer, LessonSerializer, PaymentListSerializer, PaymentDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()




class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_choice',)
    ordering_fields = ('date',)





class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()








