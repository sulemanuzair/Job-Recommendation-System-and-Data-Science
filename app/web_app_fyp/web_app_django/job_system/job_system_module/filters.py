import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class JobsFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name='start_date', lookup_expr='gte')
	end_date = DateFilter(field_name='end_date', lookup_expr='lte')
	title = CharFilter(field_name='title', lookup_expr='icontains')
	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['id', 'window_id', 'title', 'description', 'requirement', 'state', 'country', 'zip5', 'start_date', 'end_date', 'title_original', 'description_original', 'requirements_original']