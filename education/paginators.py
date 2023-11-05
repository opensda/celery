from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    """Пагинация вывода курсов"""

    page_size = 10
    page_query_param = "page_size"
    max_page_size = 50


class LessonPaginator(PageNumberPagination):
    """Пагинация вывода уроков"""

    page_size = 10
    page_query_param = "page_size"
    max_page_size = 50
