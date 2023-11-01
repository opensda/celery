from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from education.models import Course
from education.permissions import IsModerator, IsOwner
from education.serializers.course import CourseDetailSerializer, CourseSerializer, CourseListSerializer


# class CourseViewSet(viewsets.ModelViewSet):
#     serializer_class = CourseDetailSerializer
#     queryset = Course.objects.all()


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]



class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwner]

class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]