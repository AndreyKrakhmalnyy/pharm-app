from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ..views import manage

urlpatterns = {
    path('<slug:key>', manage, name='manage')
}

urlpatterns = format_suffix_patterns(urlpatterns)