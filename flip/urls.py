from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from frame import utils

from flip import views, public


admin.autodiscover()

settings_urls = [
    url(r'^phases_of_policy/$',
        views.SettingsPhasesOfPolicyView.as_view(),
        name='phases_of_policy'),

    url(r'^phases_of_policy/new/$',
        views.SettingsPhasesOfPolicyAddView.as_view(),
        name='phases_of_policy_edit'),

    url(r'^phases_of_policy/(?P<pk>\d+)/edit$',
        views.SettingsPhasesOfPolicyEditView.as_view(),
        name='phases_of_policy_edit'),

    url(r'^phases_of_policy/(?P<pk>\d+)/delete$',
        views.SettingsPhasesOfPolicyDeleteView.as_view(),
        name='phases_of_policy_delete'),

    url(r'^foresight_approaches/$',
        views.SettingsForesightApproachesView.as_view(),
        name='foresight_approaches'),

    url(r'^foresight_approaches/new$',
        views.SettingsForesightApproachesAddView.as_view(),
        name='foresight_approaches_edit'),

    url(r'^foresight_approaches/(?P<pk>\d+)/edit$',
        views.SettingsForesightApproachesEditView.as_view(),
        name='foresight_approaches_edit'),

    url(r'^foresight_approaches/(?P<pk>\d+)/delete$',
        views.SettingsForesightApproachesDeleteView.as_view(),
        name='foresight_approaches_delete'),

    url(r'^outcomes/$',
        views.SettingsOutcomesView.as_view(),
        name='outcomes'),

    url(r'^outcomes/new$',
        views.SettingsOutcomesAddView.as_view(),
        name='outcomes_edit'),

    url(r'^outcomes/(?P<pk>\d+)/edit$',
        views.SettingsOutcomesEditView.as_view(),
        name='outcomes_edit'),

    url(r'^outcomes/(?P<pk>\d+)/delete$',
        views.SettingsOutcomesDeleteView.as_view(),
        name='outcomes_delete'),

    url(r'^(?P<setting_name>[^/]+)/update_order$',
        views.SettingsUpdateOrder.as_view(),
        name='update_order'),
]

study_urls = [
    url(r'^(?P<study_type>[^/]+)/overview/$',
        views.StudiesView.as_view(),
        name='studies_overview'),

    url(r'^overview/$',
        views.StudiesView.as_view(),
        name='studies_overview'),

    url(r'^(?P<study_type>[^/]+)/new/$',
        views.StudyMetadataAddView.as_view(),
        name='study_metadata_add'),

    url(r'^new/$',
        views.StudyMetadataAddView.as_view(),
        name='study_metadata_add'),

    url(r'^(?P<study_type>[^/]+)/(?P<pk>\d+)/edit$',
        views.StudyMetadataEditView.as_view(),
        name='study_metadata_edit'),

    url(r'^(?P<study_type>[^/]+)/(?P<pk>\d+)/detail$',
        views.StudyMetadataDetailView.as_view(),
        name='study_metadata_detail'),

    url(r'^(?P<pk>\d+)/detail$',
        views.StudyMetadataDetailView.as_view(),
        name='study_metadata_detail'),

    url(r'^(?P<study_type>[^/]+)/(?P<pk>\d+)/delete$',
        views.StudyDeleteView.as_view(),
        name='study_delete'),

    url(r'^(?P<pk>\d+)/delete$',
        views.StudyDeleteView.as_view(),
        name='study_delete'),

    url(r'^(?P<study_type>[^/]+)/(?P<pk>\d+)/change/status$',
        views.StudyStatusEditView.as_view(),
        name='study_status_edit'),

    url(r'^(?P<pk>\d+)/change/status$',
        views.StudyStatusEditView.as_view(),
        name='study_status_edit'),

    url(r'^(?P<pk>\d+)/outcomes/detail$',
        views.StudyOutcomesDetailView.as_view(),
        name='study_outcomes_detail'),

    url(r'^(?P<pk>\d+)/outcomes/new$',
        views.StudyOutcomesAddView.as_view(),
        name='study_outcomes_add'),

    url(r'^(?P<pk>\d+)/outcomes/(?P<outcome_pk>\d+)/detail$',
        views.StudyOutcomeDetailView.as_view(),
        name='study_outcome_detail'),

    url(r'^(?P<pk>\d+)/outcomes/(?P<outcome_pk>\d+)/delete$',
        views.StudyOutcomeDeleteView.as_view(),
        name='study_outcome_delete'),

    url(r'^(?P<pk>\d+)/outcomes/(?P<outcome_pk>\d+)/edit$',
        views.StudyOutcomeEditView.as_view(),
        name='study_outcome_edit'),

    url(r'^(?P<pk>\d+)/outcomes/(?P<outcome_pk>\d+)/modal_edit$',
        views.StudyOutcomeEditModalView.as_view(),
        name='study_outcome_edit_modal'),

    url(r'^(?P<pk>\d+)/outcomes_section$',
        views.StudyOutcomesSectionView.as_view(),
        name='study_outcomes_section'),

]

public_urls = [
    url(r'^policy-cycle$', public.StudiesList.as_view(), name='studies_list'),
    url(r'^policy-cycle/(?P<pk>\d+)/detail$', public.StudiesDetail.as_view(),
        name='studies_detail'),
    url(r'^assessments$', public.AssessmentsList.as_view(),
        name='assessments_list'),
    url(r'^assessments/(?P<pk>\d+)/detail$', public.StudiesDetail.as_view(),
        name='assessments_detail'),
    url(r'^assessments/outcomes/(?P<outcome>\d+)$',
        public.OutcomesList.as_view(),
        name='assessments_outcomes'),
]

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name="home.html"),
        name='home_view'),

    url(r'^studies/entries/$',
        views.UserEntriesView.as_view(),
        name='user_entries'),

    url(r'^new/',
        views.StudyMetadataAddView.as_view(),
        name='add_new'),

    url(r'^studies/', include(study_urls)),

    url(r'^public/', include(public_urls, namespace='public')),

    url(r'^settings/', include(settings_urls, namespace='settings')),

    url(r'^_lastseencount/$', utils.get_objects_from_last_seen_count),

    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
