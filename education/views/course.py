from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from education.models import Course
from education.paginators import CoursePaginator
from education.permissions import IsModerator, IsOwner
from education.serializers.course import (
    CourseDetailSerializer,
    CourseSerializer,
    CourseListSerializer,
)
from education.tasks import send_upd_info


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = CoursePaginator


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsModerator | IsOwner]
    def put(self, request, *args, **kwargs):
        course_name = request.data.get("name")
        send_upd_info.delay(course_name=course_name)
        return self.update(request, *args, **kwargs)



class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]


