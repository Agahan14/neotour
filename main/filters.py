import django_filters

from .models import Tour


class TourFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(
        field_name="category__name",
        lookup_expr="iexact",
    )
    season = django_filters.CharFilter(
        field_name="season",
        lookup_expr="iexact",
    )

    class Meta:
        model = Tour
        fields = ["category_name", "season"]
