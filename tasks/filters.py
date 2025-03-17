import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()
    created_after = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    updated_after = django_filters.DateFilter(field_name="updated_at", lookup_expr="gte")

    class Meta:
        model = Task
        fields = ['completed', 'created_after', 'updated_after']
