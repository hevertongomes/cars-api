from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class MediumPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 10000

class LargePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ExtraLargePagination(PageNumberPagination):
    page_size = 70
    page_size_query_param = 'page_size'
    max_page_size = 10000

class HugePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000