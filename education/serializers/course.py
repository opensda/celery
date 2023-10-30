from rest_framework import serializers

from education.models import Course



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
