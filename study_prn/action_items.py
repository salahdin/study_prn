from edc_action_item import Action, HIGH_PRIORITY, site_action_items

DEATH_REPORT_ACTION = 'submit-death-report'


class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'study.death_report'
    show_on_dashboard = True
    priority = HIGH_PRIORITY


site_action_items.register(DeathReportAction)