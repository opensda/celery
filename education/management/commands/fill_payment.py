from django.core.management import BaseCommand

from education.models import Payment, Course
from users.models import User

"""Кастомная команда для наполнения БД"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Предварительно очищаем БД

        Payment.objects.all().delete()

        # Формируем необходимые данные для записи

        Pete = User.objects.create(email="pete@maol.com")
        Vasil = User.objects.create(email="vasil@maol.com")
        Vova = User.objects.create(email="vova@maol.com")
        Nik = User.objects.create(email="nik@maol.com")

        python = Course.objects.create(name="python")
        java = Course.objects.create(name="java")
        C_lang = Course.objects.create(name="C")
        sql = Course.objects.create(name="sql")

        payments = [
            {
                "user": Pete,
                "course": python,
                "total": 100_000,
                "payment_choice": "Наличные",
            },
            {
                "user": Vasil,
                "course": java,
                "total": 150_000,
                "payment_choice": "Перевод на счет",
            },
            {
                "user": Vova,
                "course": C_lang,
                "total": 200_000,
                "payment_choice": "Наличные",
            },
            {
                "user": Nik,
                "course": sql,
                "total": 70_000,
                "payment_choice": "Перевод на счет",
            },
        ]

        payments_to_fill = []
        for payment in payments:
            payments_to_fill.append(Payment(**payment))

        # Записываем данные

        Payment.objects.bulk_create(payments_to_fill)
