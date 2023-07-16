import django_filters
from django.db.models import Q
from django import forms

from core.models import Students


class StudentFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search',widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Students
        fields = ['search']
    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(standard__icontains=value) |
            Q(address=value)
        )
