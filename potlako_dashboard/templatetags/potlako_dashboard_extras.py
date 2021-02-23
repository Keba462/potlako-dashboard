from django import template
from django.conf import settings
from edc_base.utils import get_utcnow

register = template.Library()


@register.inclusion_tag('potlako_dashboard/buttons/screening_button.html')
def screening_button(model_wrapper):
    return dict(
        add_screening_href=model_wrapper.subject_screening.href,
        screening_identifier=model_wrapper.object.screening_identifier,
        subject_screening_obj=model_wrapper.subject_screening_model_obj)
    
@register.inclusion_tag('potlako_dashboard/buttons/verbal_consent_button.html')
def verbal_consent_button(model_wrapper):
    return dict(
        add_screening_href=model_wrapper.subject_screening.href,
        screening_identifier=model_wrapper.object.screening_identifier,
        subject_screening_obj=model_wrapper.subject_screening_model_obj,
        verbal_consent_url=settings.DASHBOARD_URL_NAMES.get('verbal_consent_url'))
    
@register.inclusion_tag('potlako_dashboard/buttons/verbal_consent_pdf_button.html')
def verbal_consent_pdf_button(model_wrapper):
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        verbal_consent_pdf_url=model_wrapper.verbal_consent_pdf_url)


@register.inclusion_tag('potlako_dashboard/buttons/clinician_call_enrollment_button.html')
def clinician_call_enrollment_button(model_wrapper):
    title = ['Edit Clinician Call Enrollment form.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('potlako_dashboard/buttons/eligibility_button.html')
def eligibility_button(model_wrapper):
    comment = []
    obj = model_wrapper.subject_screening_model_obj or model_wrapper.object
    tooltip = None
    if not obj.is_eligible and obj.ineligibility:
        comment = obj.ineligibility.strip('[').strip(']').split(',')
    comment = list(set(comment))
    comment.sort()
    return dict(is_eligible=obj.is_eligible, comment=comment, tooltip=tooltip)


@register.inclusion_tag('potlako_dashboard/buttons/subject_locator_button.html')
def subject_locator_button(model_wrapper):
    title = ['Add subject Locator.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_subject_locator_href=model_wrapper.subject_locator.href,
        subject_locator_model_obj=model_wrapper.subject_locator_model_obj,
        title=' '.join(title))

@register.inclusion_tag('potlako_dashboard/buttons/baseline_clinical_summary_button.html')
def baseline_clinical_summary_button(model_wrapper, groups):
    title = ['Add baseline clinical summary.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_baseline_summary_href=model_wrapper.baseline_summary.href,
        baseline_summary_model_obj=model_wrapper.baseline_summary_model_obj,
        readonly='RA' in groups,
        title=' '.join(title))


@register.inclusion_tag('potlako_dashboard/buttons/baseline_clinical_summary_button.html')
def baseline_clinical_summary_btn(model_wrapper):
    title = ['Add baseline clinical summary.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_baseline_summary_href=model_wrapper.baseline_summary.href,
        baseline_summary_model_obj=model_wrapper.baseline_summary_model_obj,
        title=' '.join(title))


@register.inclusion_tag('potlako_dashboard/buttons/navigation_plan_summary_button.html')
def navigation_plan_summary_button(model_wrapper, groups):
    title = ['Add navigation summary and plan.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_navigation_plan_summary_href=model_wrapper.navigation_plan_summary.href,
        navigation_plan_summary_model_obj=model_wrapper.navigation_plan_summary_model_obj,
        readonly='RA' in groups,
        title=' '.join(title))


@register.inclusion_tag('potlako_dashboard/buttons/navigation_plan_summary_button.html')
def navigation_plan_summary_btn(model_wrapper):
    title = ['Add navigation summary and plan.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_navigation_plan_summary_href=model_wrapper.navigation_plan_summary.href,
        navigation_plan_summary_model_obj=model_wrapper.navigation_plan_summary_model_obj,
        title=' '.join(title))

@register.inclusion_tag('potlako_dashboard/buttons/cancer_dx_endpoint_button.html')
def cancer_dx_endpoint_button(model_wrapper):
    title = ['Add cancer diagnosis and treatment endpoint recording.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_cancer_dx_endpoint_href=model_wrapper.cancer_dx_endpoint.href,
        cancer_dx_endpoint_model_obj=model_wrapper.cancer_dx_endpoint_model_obj,
        title=' '.join(title))

@register.inclusion_tag('potlako_dashboard/buttons/care_seeking_endpoint_button.html')
def care_seeking_endpoint_button(model_wrapper):
    title = ['Add symptoms and care seeking endpoint recording.']
    return dict(
        subject_identifier=model_wrapper.subject_identifier,
        add_care_seeking_endpoint_href=model_wrapper.care_seeking_endpoint.href,
        care_seeking_endpoint_model_obj=model_wrapper.care_seeking_endpoint_model_obj,
        title=' '.join(title))

@register.inclusion_tag('potlako_dashboard/buttons/consent_button.html')
def consent_button(model_wrapper):
    title = ['Consent subject to participate.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        subject_identifier=model_wrapper.subject_identifier,
        subject_screening_obj=model_wrapper.subject_screening_model_obj,
        add_consent_href=model_wrapper.consent.href,
        consent_version=model_wrapper.consent_version,
        title=' '.join(title))


@register.inclusion_tag('potlako_dashboard/buttons/dashboard_button.html')
def dashboard_button(model_wrapper):
    subject_dashboard_url = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')
    return dict(
        subject_dashboard_url=subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier)
