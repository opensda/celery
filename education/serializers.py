from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson, Payment
from users.models import User


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("name",)




class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()


    class Meta:
        model = Course
        fields = '__all__'

    # Выводим поле уроков, которые есть на курсе
    def get_lessons(self, course):
        return [lesson.name for lesson in course.lesson.all()]

    # Выводим количество уроков в курсе
    def get_lessons_count(self, course):

        return course.lesson.count()



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):

    # Меняем id курса на его название

    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'



class PaymentListSerializer(serializers.ModelSerializer):


    # Меняем id курса на его название

    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    # Меняем id пользователя на его почту

    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentDetailSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
