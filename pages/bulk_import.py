from playwright.sync_api import Page
from playwright.sync_api import expect

import pyautogui
import os

class BulkImportPage:
    def __init__(self, page: Page):
        self.page = page

    def select_service(self, sigla, service):
        print("\n ------------------------------------------------------------ \n")
        print(f"\n Iniciando automação da calculadora sigla: {sigla} \n")
        select_service = self.page.locator("//span[contains(text(), 'Escolher um serviço')]")
        select_service.click(timeout=60000)

        ec2_instance_option = self.page.locator(f"//span[contains(text(), '{service}')]")
        ec2_instance_option.click()
    
    def input_field(self, sigla):
        input_field = self.page.locator("//input[@placeholder='Insira um nome de grupo']")
        input_field.fill(sigla)

    def upload_file(self, sigla):
        upload_input = self.page.locator("//button[@aria-label='Carregar modelo de importação em massa']")
        upload_input.click()

        # pastas = ["documentos", "repositorios", "playwright-with-python", "siglas"]
        pastas = ["Documents"]

        for pasta in pastas:
            pyautogui.write(pasta)
            pyautogui.press("enter")

        file_name = f"{sigla}_AWS.xlsx"
        file_path = os.path.join(os.getcwd()+ "/siglas/", file_name)

        if os.path.exists(file_path):
            print(f"Fazendo upload do arquivo: {file_name} \n")
            pyautogui.write(file_name)
            pyautogui.press("enter")

            file_success = self.page.locator("//span[@aria-label='sucesso']")
            expect(file_success).to_be_visible(timeout=50000)

            if file_success:
                print("Upload realizado com sucesso")
            else:
                print("Erro ao realizar upload")

        else:
            print(f"O arquivo com a sigla '{sigla}' não existe.")
            pyautogui.hotkey("command", "w")

        print("\n ------------------------------------------------------------ \n")

    def save_and_view_resume(self):
        save_and_view_resume = self.page.locator("//button[@aria-label='Salvar e visualizar resumo']")
        save_and_view_resume.click()