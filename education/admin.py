from django.contrib import admin

from education.models import Course, Lesson, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'user',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'video_link', 'course',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'lesson', 'total', 'payment_choice',)


