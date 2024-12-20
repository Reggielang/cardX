import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import MdCardFilter
from .models import TrainerCard, MdCard, PokemonCard, TrainerCardSerializer, PokemonCardSerializer, MdCardSerializer

logger = logging.getLogger(__name__)

# 分页查询设置
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100  # 设置最大页面大小限制


class TrainerCardListView(ListAPIView):
    queryset = TrainerCard.objects.all()
    serializer_class = TrainerCardSerializer
    pagination_class = StandardResultsSetPagination


class PokemonCardListView(ListAPIView):
    queryset = PokemonCard.objects.all()
    serializer_class = PokemonCardSerializer
    pagination_class = StandardResultsSetPagination


class MdCardListView(ListAPIView):
    queryset = MdCard.objects.all()
    serializer_class = MdCardSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class  = MdCardFilter  # 使用我们创建的过滤器类

