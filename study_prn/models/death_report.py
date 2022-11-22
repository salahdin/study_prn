from django.db import models

from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.sites import SiteModelMixin
from edc_base.sites.managers import CurrentSiteManager
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import date_not_before_study_start
from ..choice import CAUSE_OF_DEATH

from ..action_items import DEATH_REPORT_ACTION


class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):
    action_name = DEATH_REPORT_ACTION

    tracking_identifier_prefix = 'DR'

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    death_date = models.DateField(
        verbose_name='Date of Death:',
        validators=[
            date_not_before_study_start,
            date_not_future,
        ],
        help_text='',
    )

    cause_of_death = models.CharField(
        verbose_name='What is the primary source of cause of death '
                     'information?',
        max_length=50,
        choices=CAUSE_OF_DEATH, )

    cause_of_death_other = models.CharField(
        verbose_name='Other, specify',
        max_length=50,
        blank=True,
        null=True)

    comment = models.TextField(
        max_length=500,
        verbose_name='Comments',
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'study_prn'
        verbose_name = 'Death Report'
