from playwright.sync_api import Page
from pages.bulk_import import *
from pages.estimate import *
from pages.template import *
from setup import *
from input.user_input import sigla, service


def test_calculadora(page: Page):
    setup = Start(page)
    template_page = TemplatePage(page)
    bulkimport_page = BulkImportPage(page)
    estimate_page = EstimatePage(page)

    setup.start()

    template_page.confirm_language()
    template_page.update_template(sigla)

    bulkimport_page.select_service(service)
    bulkimport_page.input_field(sigla)
    bulkimport_page.upload_file(sigla)
    bulkimport_page.save_and_view_resume()

    estimate_page.view_page_estimate()
    estimate_page.edit_name_estimate(sigla)
    estimate_page.resources_ec2()
    estimate_page.resources_alb()
    estimate_page.environments(sigla)
    estimate_page.shared(sigla)
