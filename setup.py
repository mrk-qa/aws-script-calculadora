from playwright.sync_api import Page

class Start:

    def __init__(self, page: Page):
        self.page = page

    def start(self):
        URL_TEMPLATE = "https://calculator.aws/#/estimate?id=a70ac3549ad99f2b810f24470529314d4c9420d2"

        self.page.set_default_timeout(60000)
        self.page.set_default_navigation_timeout(60000)
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.page.goto(URL_TEMPLATE)
