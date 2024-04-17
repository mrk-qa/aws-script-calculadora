from playwright.sync_api import Page
from playwright.sync_api import expect
 
import pyautogui
import os
import platform

class BulkImportPage:
    def __init__(self, page: Page):
        self.page = page

    def select_service(self):
        select_service = self.page.locator("//span[contains(text(), 'Escolher um serviço')]")
        select_service.click()

        ec2_instance_option = self.page.locator(f"//span[contains(text(), 'Instâncias do EC2')]")
        ec2_instance_option.click()
    
    def input_field(self, sigla):
        input_field = self.page.locator("//input[@placeholder='Insira um nome de grupo']")
        input_field.fill(sigla)

    def upload_file(self, sigla):
        upload_input = self.page.locator("//button[@aria-label='Carregar modelo de importação em massa']")
        upload_input.click()

        self.page.wait_for_timeout(3000)

        operating_system = platform.system()
        
        if operating_system == "Windows":
            file_path_windows = os.getcwd() + "\\siglas"
            pyautogui.write(file_path_windows)
            pyautogui.press("enter")
        else:
            pastas = ["documentos", "migration", "script-calculadora", "siglas"]

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
        save_and_view_resume = self.page.locator("//div[@class='appFooter']//button[@aria-label='Salvar e visualizar resumo']")
        save_and_view_resume.click()