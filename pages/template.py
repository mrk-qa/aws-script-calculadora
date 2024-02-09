from playwright.sync_api import Page

class TemplatePage:
    def __init__(self, page: Page):
        self.page = page

    def confirm_language(self):
        self.page.wait_for_timeout(5000)
        get_language = self.page.locator("//div[@data-cy='calculator-navigation']//button[@aria-label='Language: English']")
        language_text = get_language.inner_text()

        if language_text == "Language: English":
            get_language.click()
            select_language = self.page.locator("//li[@data-testid='pt_BR']")
            select_language.click()

    def update_template(self, sigla):
        print("\n ------------------------------------------------------------ \n")
        print(f"Iniciando automação da calculadora sigla: {sigla} \n")

        update_estimate = self.page.locator("//button[@aria-label='Botão Atualizar estimativa']")
        update_estimate.click()

        add_service = self.page.locator("//button[@aria-label='Adicionar serviço']")
        add_service.click()

        bulk_import = self.page.locator("//a[@aria-label='Importação em massa']")
        bulk_import.click()
