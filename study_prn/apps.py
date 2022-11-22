from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'study_prn'
    verbose_name = 'Study prn'
    admin_site_name = 'study_prn_admin'
