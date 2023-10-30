from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views.course import CourseViewSet, CourseRetrieveAPIView
from education.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from education.views.payment import PaymentListAPIView, PaymentRetrieveAPIView

app_name = EducationConfig.name

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('courses/<int:pk>', CourseRetrieveAPIView.as_view(), name='course_retrieve'),

                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
                  path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),

              ] + router.urls
