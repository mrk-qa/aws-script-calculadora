from playwright.sync_api import sync_playwright
from pages.bulk_import import *
from pages.estimate import *
from pages.template import *

try:
    from data.data_processing import sigla
except ImportError:
    exit(1)

with sync_playwright() as p:
    chromium_path = os.path.abspath("browser/chrome/chrome.exe")
    browser = p.chromium.launch(executable_path=chromium_path, headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)
    page.goto("https://calculator.aws/#/estimate?id=a70ac3549ad99f2b810f24470529314d4c9420d2")

    template_page = TemplatePage(page)
    bulkimport_page = BulkImportPage(page)
    estimate_page = EstimatePage(page)
    
    template_page.confirm_language()
    template_page.update_template(sigla)
 
    bulkimport_page.select_service()
    bulkimport_page.input_field(sigla)
    bulkimport_page.upload_file(sigla)
    bulkimport_page.save_and_view_resume()
 
    estimate_page.view_page_estimate()
    estimate_page.edit_name_estimate(sigla)
    estimate_page.resources_ec2()
    estimate_page.resources_alb()
    estimate_page.environments(sigla)
    estimate_page.shared(sigla)