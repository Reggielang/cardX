import django_filters
from .models import MdCard,TrainerCard,PokemonCard

class MdCardFilter(django_filters.FilterSet):
    # 你可以在这里添加自定义过滤规则，例如：
    ch_name = django_filters.CharFilter(field_name='ch_name',  lookup_expr='icontains')  # 模糊匹配名字
    card_type = django_filters.CharFilter(field_name='card_type', lookup_expr='exact')  # 精确匹配类型
    card_number = django_filters.CharFilter(field_name='card_number', lookup_expr='icontains')  # 卡牌编号精确匹配

    class Meta:
        model = MdCard
        fields = ['ch_name', 'card_type','card_number']

class PokemonCardFilter(django_filters.FilterSet):
    # 你可以在这里添加自定义过滤规则，例如：
    name = django_filters.CharFilter(field_name='name',  lookup_expr='icontains')  # 模糊匹配名字
    type = django_filters.CharFilter(field_name='type', lookup_expr='exact')  # 精确匹配类型
    weakness = django_filters.CharFilter(field_name='weakness', lookup_expr='exact')  # 精确匹配类型
    card_number = django_filters.CharFilter(field_name='card_number', lookup_expr='icontains')  # 卡牌编号精确匹配

    class Meta:
        model = PokemonCard
        fields = ['name', 'type','card_number','weakness']

class TrainerCardFilter(django_filters.FilterSet):
    # 你可以在这里添加自定义过滤规则，例如：
    name = django_filters.CharFilter(field_name='name',  lookup_expr='icontains')  # 模糊匹配名字
    type = django_filters.CharFilter(field_name='type', lookup_expr='exact')  # 精确匹配类型
    card_number = django_filters.CharFilter(field_name='card_number', lookup_expr='icontains')  # 卡牌编号精确匹配

    class Meta:
        model = TrainerCard
        fields = ['name', 'type','card_number']