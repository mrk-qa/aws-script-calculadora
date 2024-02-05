from playwright.sync_api import Page

class Start:
    URL = "https://calculator.aws/#/bulk-import"

    def __init__(self, page: Page):
        self.page = page
        # context = self.page.context

    def start(self):
        self.page.set_default_timeout(60000)
        self.page.set_default_navigation_timeout(600000)
        self.page.set_viewport_size({"width": 1600, "height": 1000})
        self.page.goto(self.URL)
        
    def continue_url(self, sigla):
        self.page.set_default_timeout(60000)
        self.page.set_default_navigation_timeout(600000)
        self.page.set_viewport_size({"width": 1600, "height": 1000})

        with open(f"url/url_{sigla}.txt", "r") as f:
            url_read = f.read().strip()

        url = url_read

        self.page.goto(url)
        self.page.context.clear_cookies()