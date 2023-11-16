from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="название курса")
    image = models.ImageField(
        upload_to="courses/", verbose_name="изображение", **NULLABLE
    )
    description = models.TextField(verbose_name="описание курса", **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="название урока")
    image = models.ImageField(
        upload_to="lessons/", verbose_name="изображение", **NULLABLE
    )
    description = models.TextField(verbose_name="описание урока", **NULLABLE)
    video_link = models.TextField(verbose_name="ссылка на видео", **NULLABLE)
    course = models.ForeignKey(
        Course, related_name="lesson", on_delete=models.SET_NULL, **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )
    date = models.DateTimeField(verbose_name="дата оплаты", **NULLABLE)
    course = models.ForeignKey(
        Course,
        verbose_name="оплаченный курс",
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name="оплаченный урок",
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    total = models.FloatField(verbose_name="сумма оплаты", **NULLABLE)

    payment_mode = [
        ("наличные", "Наличные"),
        ("перевод на счет", "Перевод на счет"),
    ]
    payment_choice = models.CharField(
        max_length=50, choices=payment_mode, verbose_name="способ оплаты", **NULLABLE
    )
    is_confirmed = models.BooleanField(
        default=False, verbose_name="подтверждение оплаты"
    )

    def __str__(self):
        return (
            f"{self.user}, {self.total}: {self.lesson if self.lesson else self.course}"
        )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

        ordering = ("date",)


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь",
        related_name='subsription', **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        verbose_name="подписка на курс",
        related_name="subscription",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}, {self.course}: {self.is_subscribed}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
