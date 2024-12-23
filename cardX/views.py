import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .filters import MdCardFilter, PokemonCardFilter, TrainerCardFilter
from .models import (TrainerCard, MdCard, PokemonCard,TrainerCardBasicSerializer,TrainerCardDetailSerializer,MdCardBasicSerializer
,PokemonCardBasicSerializer,MdCardDetailSerializer,PokemonCardDetailSerializer)

logger = logging.getLogger(__name__)

# 分页查询设置
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100  # 设置最大页面大小限制


class TrainerCardListView(ListAPIView):
    queryset = TrainerCard.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class  = TrainerCardFilter  # 使用我们创建的过滤器类
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        # 根据查询参数选择序列化器
        detail_level = self.request.query_params.get('detail', 'basic').lower()
        if detail_level == 'detail':
            serializer_class = TrainerCardDetailSerializer
        else:
            serializer_class = TrainerCardBasicSerializer

        return serializer_class


class PokemonCardListView(ListAPIView):
    queryset = PokemonCard.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class  = PokemonCardFilter  # 使用我们创建的过滤器类
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        # 根据查询参数选择序列化器
        detail_level = self.request.query_params.get('detail', 'basic').lower()
        if detail_level == 'detail':
            serializer_class = PokemonCardDetailSerializer
        else:
            serializer_class = PokemonCardBasicSerializer

        return serializer_class


class MdCardListView(ListAPIView):
    queryset = MdCard.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class  = MdCardFilter  # 使用我们创建的过滤器类
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        # 根据查询参数选择序列化器
        detail_level = self.request.query_params.get('detail', 'basic').lower()
        if detail_level == 'detail':
            serializer_class = MdCardDetailSerializer
        else:
            serializer_class = MdCardBasicSerializer

        return serializer_class

