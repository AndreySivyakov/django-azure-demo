from .models import *
import django_filters
from django import forms
#from django_select2.forms import Select2Widget
#from dal import autocomplete

class ClaimFilter(django_filters.FilterSet):
    responsible_rep = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Claim
        fields = ['responsible_rep', 'status',]
        widgets = {'status': forms.Select,}

class VendorFilter(django_filters.FilterSet):
    class Meta:
        model = Vendor
        fields = ['vendor_name', ]
