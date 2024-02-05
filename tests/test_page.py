from playwright.sync_api import Page
from pages.bulk_import import *
from pages.estimate import *
from setup import *
from input.user_input import sigla, service

# Teste 1 que gera a url da calculadora
def test_calculadora_1(page : Page):
    setup = Start(page)
    bulkimport_page = BulkImportPage(page)
    estimate_page = EstimatePage(page)

    setup.start()

    bulkimport_page.select_service(sigla, service)
    bulkimport_page.input_field(sigla)
    bulkimport_page.upload_file(sigla)
    bulkimport_page.save_and_view_resume()

    estimate_page.view_page_estimate()
    estimate_page.edit_name_estimate(sigla)
    # estimate_page.resources_ec2()
    estimate_page.resources_alb()
    estimate_page.environments(sigla)
    estimate_page.shared(sigla)

    page.screenshot(path=f"reports/screenshot_{sigla}.png", full_page=True)

# Continuação do teste 1, que pega a url da calculadora e edita apenas as EC2
def test_get_url(page : Page):
    setup = Start(page)
    estimate_page = EstimatePage(page)

    setup.continue_url(sigla)

    estimate_page.update_estimate()
    estimate_page.resources_ec2()
    estimate_page.shared(sigla)