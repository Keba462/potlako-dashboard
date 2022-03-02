import re

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView as BaseListboardView

from ...model_wrappers import SubjectConsentModelWrapper
from .filters import ListboardViewFilters


class ListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                    ListboardFilterViewMixin, SearchFormViewMixin, BaseListboardView):

    listboard_template = 'endpoint_listboard_template'
    listboard_url = 'endpoint_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"
    # permission_required = 'potlako_subject.add_cancerdxandtxendpoint'

    listboard_view_filters = ListboardViewFilters()
    model = 'potlako_subject.subjectconsent'
    model_wrapper_cls = SubjectConsentModelWrapper
    navbar_name = 'potlako_dashboard'
    navbar_selected_item = 'endpoint_recordings'
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'endpoint_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        print()
        context = super().get_context_data(**kwargs)
        context.update(
            cancer_diagnoses_and_treatment_add_url=self.model_cls().get_absolute_url())
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        return options

    def get_queryset(self):
        filter_options = self.get_queryset_filter_options(
            self.request, *self.args, **self.kwargs)
        for field, value in filter_options.items():
            if len(field.split(".")) > 1:
                model, field_name = field.split(".")
                model_cls = django_apps.get_model(f'potlako_subject.{model}')
                queryset = model_cls.objects.filter(
                    **{f'{field_name}': value}).values_list(
                    'subject_identifier', flat=True)
                consent_model = django_apps.get_model(
                    'potlako_subject.subjectconsent')
                query = consent_model.objects.filter(
                    subject_identifier__in=queryset)
                return query
        return super().get_queryset()

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
