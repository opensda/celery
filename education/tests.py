import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты на CRUD уроков"""

    def setUp(self):
        """Добавляем урок в БД для тестирования"""
        self.lesson = Lesson.objects.create(name="test")

    def test_get_lesson_list(self):
        response = self.client.get(reverse("education:lesson_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "course": None,
                        "name": self.lesson.name,
                        "image": self.lesson.image,
                        "description": self.lesson.description,
                        "video_link": self.lesson.video_link,
                    }
                ],
            },
        )

    def test_lesson_create(self):
        data = {
            "name": "test2",
            "video_link": "https://www.youtube.com/watch?v=NjJx6B5De8g",
        }

        response = self.client.post(reverse("education:lesson_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_validation(self):
        """Тест на валидацию ссылки"""

        data = {
            "name": "test3",
            "video_link": "https://my.sky.pro/student-cabinet/stream-lesson/94980/theory/10",
        }

        response = self.client.post(reverse("education:lesson_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"video_link": ["Ссылку можно размещать только на youtube.com"]},
        )

    def test_lesson_update(self):
        data = {
            "name": "test_4",
            "video_link": "https://www.youtube.com/watch?v=NjJx6B5De8g",
        }

        url = reverse("education:lesson_update", args=[self.lesson.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_deletion(self):
        url = reverse("education:lesson_delete", args=[self.lesson.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubsciptionTestCase(APITestCase):
    """Тесты на CRUD подписки"""

    def setUp(self):
        self.user = User.objects.create(email="developer@java.com")

        self.course = Course.objects.create(name="JAVASCRIPT")
        self.subsciption = Subscription.objects.create(
            user=self.user, course=self.course, is_subscribed=False
        )

    def test_get_subscription_list(self):
        response = self.client.get(reverse("education:subscription_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_update(self):
        data = {"user": 3, "course": 3, "is_subscribed": True}

        url = reverse("education:subscription_update", args=[self.subsciption.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_deletion(self):
        url = reverse("education:subscription_delete", args=[self.subsciption.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
