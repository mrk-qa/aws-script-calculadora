from playwright.sync_api import Page
from screeninfo import get_monitors

class Start:

    def __init__(self, page: Page):
        self.page = page

    def start(self):
        monitor = get_monitors()[0]
        width, height = monitor.width, monitor.height

        URL_TEMPLATE = "https://calculator.aws/#/estimate?id=a70ac3549ad99f2b810f24470529314d4c9420d2"

        self.page.set_default_timeout(60000)
        self.page.set_default_navigation_timeout(60000)
        self.page.set_viewport_size({ "width": width, "height": height })
        self.page.goto(URL_TEMPLATE)
