from django.contrib import admin

from education.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "image",
        "description",
        "user",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "image",
        "description",
        "video_link",
        "course",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "date",
        "course",
        "lesson",
        "total",
        "payment_choice",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "course",
        "is_subscribed",
    )
