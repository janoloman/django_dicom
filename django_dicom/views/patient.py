from django_dicom.filters import PatientFilter
from django_dicom.models import Patient
from django_dicom.serializers import PatientSerializer
from django_dicom.views.defaults import DefaultsMixin
from django_dicom.views.pagination import StandardResultsSetPagination
from rest_framework import viewsets


class PatientViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    
    """

    filter_class = PatientFilter
    pagination_class = StandardResultsSetPagination
    queryset = Patient.objects.all().order_by("family_name", "given_name")
    serializer_class = PatientSerializer

