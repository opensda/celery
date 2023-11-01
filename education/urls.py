from django.urls import path

from education.apps import EducationConfig

from education.views.course import CourseRetrieveAPIView, CourseCreateAPIView, CourseListAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView
from education.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from education.views.payment import PaymentListAPIView, PaymentRetrieveAPIView

app_name = EducationConfig.name

urlpatterns = [

    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_retrieve'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_delete'),

    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
]
