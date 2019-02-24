import django_filters
from portal.models import Candidate


class CandidateFilter(django_filters.FilterSet):
    class Meta:
        model = Candidate
        fields = ['qualification', 'industry', 'experience', 'roles', 'city', 'skills']
