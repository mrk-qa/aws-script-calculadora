from playwright.sync_api import Page
from playwright.sync_api import expect
from data.data_processing import *
 
class EstimatePage:
    def __init__(self, page: Page):
        self.page = page
 
    def view_page_estimate(self):
        my_estimate = self.page.locator("//h1")
        expect(my_estimate).to_have_text("Template")
 
    def edit_name_estimate(self, sigla):
        edit_name_estimate = self.page.locator("//span[@aria-label='Edit My Estimate']")
        edit_name_estimate.click()
 
        name_estimate = self.page.locator("//input[@aria-label='Enter Name']")
        name_estimate.click()
        name_estimate.fill("Sigla " + sigla)
 
        save_name_estimate = self.page.locator("//button[@aria-label='Salvar']")
        save_name_estimate.click()
 
        print("Alterado o nome da estimativa da calculadora com sucesso")
 
        print("\n ------------------------------------------------------------ \n")
 
    def resources_ec2(self):
        environments = self.page.query_selector_all("li [data-parent-group='true'] p")
        qtde_environments = len(environments)
 
        e = 1
        while e <= qtde_environments:
   
            each_environment = self.page.locator(f"li [data-parent-group='true']:nth-child({e}) p").all()
            environment_name = each_environment[0].inner_text()
 
            for environment in each_environment:
                print(f"Acessando ambiente {e}: {environment_name} \n")
                self.page.wait_for_timeout(3000)
                self.page.reload()
                self.page.wait_for_timeout(3000)
 
                environment.click()
            
                resources = self.page.query_selector_all("//tr[@data-selection-item='item']")
                qtde_resources = len(resources)
                
                r = 1
                while r <= qtde_resources:
                    each_edits = self.page.locator(f"tr[data-selection-item='item']:nth-child({r}) :nth-child(2) [data-cy='edit-service']").all()
 
                    for edit in each_edits:
                        
                        print(f"Editando EC2 {r} no ambiente {environment_name} \n")
                        edit.click()
                        self.page.wait_for_timeout(3000)
 
                        find = self.page.locator("//div[@class='show']/span[4]/div/div")
                        find.click()
 
                        check = self.page.locator("//input[@aria-label='Habilitar monitoramento']/..")
                        check.click()
                        self.page.wait_for_timeout(3000)
 
                        update = self.page.locator("//button[@aria-label='Atualizar']")
                        update.click()
 
                    r += 1
 
                print(" ------------------------------------------------------------ \n")
 
            e += 1
 
    def resources_alb(self):
        environments = self.page.query_selector_all("li [data-parent-group='true'] p")
        qtde_environments = len(environments)
        
        e = 1
        while e <= qtde_environments:
            each_environment = self.page.locator(f"li [data-parent-group='true']:nth-child({e}) p").all()
            environment_name = each_environment[0].inner_text()
 
            count_webservers = 0
 
            for environment in each_environment:
                print(f"Acessando ambiente {e}: {environment_name} para validar as EC2")
                environment.click()
 
                resources = self.page.query_selector_all("//tr[@data-selection-item='item']")
                qtde_resources = len(resources)
 
                w = 1
                while w <= qtde_resources:
                    each_webservers = self.page.locator(f"tr[data-selection-item='item']:nth-child({w}) :nth-child(6) span button span p").all()
                    
                    for webserver in each_webservers:
                        describe_server = webserver.inner_text()
                        count_webservers += describe_server.count("WEB SERVERS")
 
                    w += 1
 
            if count_webservers > 0:
                print(f"\n Foi identificado que o ambiente possui {count_webservers} EC2 sendo WEB SERVERS \n")
 
                add_service = self.page.locator("//button[@aria-label='Adicionar serviço']")
                add_service.click()
 
                name_service = self.page.locator("//input[@aria-label='Localizar serviço']")
                name_service.click()
                name_service.fill("Elastic Load Balancing")
 
                configure_alb = self.page.locator("//button[@aria-label='Configurar Elastic Load Balancing']")
                configure_alb.click()
 
                add_description = self.page.locator("//input[@aria-label='Description - optional']")
                add_description.click()
                add_description.fill("ALB")
 
                select_region = self.page.locator("//div[@data-cy='region-enhanced-dropdown']//button")
                select_region.click()
                self.page.keyboard.type("São Paulo")
                self.page.keyboard.press("ArrowDown")
                self.page.keyboard.press("Enter")
 
                add_qtde_alb = self.page.locator("//input[@aria-label='Número de Application Load Balancers']")
                add_qtde_alb.click()
                add_qtde_alb.fill(f"{count_webservers}")
 
                new_conections_alb = self.page.locator("//input[@aria-label='Número médio de novas conexões por ALB Valor']")
                new_conections_alb.click()
                new_conections_alb.fill("1000")
                self.page.keyboard.press("Tab")
                self.page.keyboard.press("Enter")
                self.page.keyboard.press("ArrowDown")
                self.page.keyboard.press("Enter")
 
                self.page.wait_for_timeout(3000)
 
                save_and_view_resume = self.page.locator("//button[@aria-label='Salvar e visualizar resumo']")
                save_and_view_resume.click()
 
                print("Recurso: Elastic Load Balacing foi adicionado com sucesso")
                print("\n ------------------------------------------------------------ \n")
 
            else:
                print("\n Foi identificado que não existem WEBSERVERS e por isso não foi adicionado ALB")
 
                print("\n ------------------------------------------------------------ \n")
 
            e += 1
 
    def environments(self, sigla):
        sigla_envionments = self.page.locator(f"//li//p[contains(text(), '{sigla}')]")
        sigla_envionments.click()
 
        select_environment = self.page.query_selector_all("tr[data-selection-item='item'] button strong")
        qtde_environments = len(select_environment)
        environment_name = select_environment[0].inner_text()
 
        development = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Development']")
        homologation = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Homologation']")
        pre_production = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Pre-Production']")
        production = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Production']")
 
        print ("Validando os ambientes \n")
 
        if pre_production.is_visible():
            print("Identificado ambiente de Pre-Production \n")
 
            if qtde_environments == 4:
                print("Já existem 4 ambientes estimados")
                print("\n ------------------------------------------------------------ \n")
 
            elif development.is_visible() and qtde_environments == 3:
                print("Criando ambiente HOMOLOGATION \n")
                select_environment_dev = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Development']")
                select_environment_dev.click()
 
                duplicated_dev = self.page.locator("//button[@aria-label='Duplicar']")
                duplicated_dev.click()
 
                select_environment_dev = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Development']")
                select_environment_dev.click()
                
                edit_dev_copy = self.page.locator("//button[@aria-label='edit Development_copy']")
                edit_dev_copy.click()
 
                input_group_name = self.page.locator("//input[@value='Development_copy']")
                input_group_name.click()
                input_group_name.fill("Homologation")
 
                save_group_name = self.page.locator("//button[@aria-label='Salvar']")
                save_group_name.click()
 
                print("Ambiente HOMOLOGATION foi criado com sucesso")
                print("\n ------------------------------------------------------------ \n")
 
            elif homologation.is_visible() and qtde_environments == 3:
                print("Criando ambiente DEVELOPMENT \n")
                select_environment_homol = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Homologation']")
                select_environment_homol.click()
                
                duplicated_homol = self.page.locator("//button[@aria-label='Duplicar']")
                duplicated_homol.click()
 
                select_environment_homol = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Homologation']")
                select_environment_homol.click()
 
                edit_homol_copy = self.page.locator("//button[@aria-label='edit Homologation_copy']")
                edit_homol_copy.click()
 
                input_group_name = self.page.locator("//input[@value='Homologation_copy']")
                input_group_name.click()
                input_group_name.fill("Development")
 
                save_group_name = self.page.locator("//button[@aria-label='Salvar']")
                save_group_name.click()
 
                print("Ambiente DEVELOPMENT foi criado com sucesso")
                print("\n ------------------------------------------------------------ \n")
 
            elif qtde_environments == 2:
                print(f"ATENÇÃO! Existe o ambiente Pre-Production na sigla {sigla}, porém não possui os 4 ambientes estimados. \n Você deve estimar os ambientes manualmente conforme necessário")
                print("\n ------------------------------------------------------------ \n")
 
                show_warning_message("Aviso", f"ATENÇÃO! Existe o ambiente Pre-Production na sigla {sigla}, porém não possui os 4 ambientes estimados. \n\nVocê deve estimar os ambientes manualmente conforme necessário")
 
        else:
 
            if qtde_environments == 3:
                print("Já existem 3 ambientes estimados")
                print("\n ------------------------------------------------------------ \n")
            
            elif qtde_environments == 1:
                print(f"ATENÇÃO! Só existe o ambiente {environment_name} na sigla {sigla}. \n Você deve estimar os ambientes manualmente conforme necessário")
                print("\n ------------------------------------------------------------ \n")
 
                show_warning_message("Aviso", f"ATENÇÃO! Só existe o ambiente {environment_name} na sigla {sigla}. \n\nVocê deve estimar os ambientes manualmente conforme necessário")
 
            elif homologation.is_visible() and qtde_environments == 2:
                print("Criando ambiente DEVELOPMENT \n")
                select_environment_homol = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Homologation']")
                select_environment_homol.click()
                
                duplicated_homol = self.page.locator("//button[@aria-label='Duplicar']")
                duplicated_homol.click()
 
                select_environment_homol = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Homologation']")
                select_environment_homol.click()
 
                edit_homol_copy = self.page.locator("//button[@aria-label='edit Homologation_copy']")
                edit_homol_copy.click()
 
                input_group_name = self.page.locator("//input[@value='Homologation_copy']")
                input_group_name.click()
                input_group_name.fill("Development")
 
                save_group_name = self.page.locator("//button[@aria-label='Salvar']")
                save_group_name.click()
 
                print("Ambiente DEVELOPMENT foi criado com sucesso")
                print("\n ------------------------------------------------------------ \n")
 
            elif development.is_visible() and qtde_environments == 2:
                print("Criando ambiente HOMOLOGATION \n")
                select_environment_dev = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Development']")
                select_environment_dev.click()
 
                duplicated_dev = self.page.locator("//button[@aria-label='Duplicar']")
                duplicated_dev.click()
 
                select_environment_dev = self.page.locator("//label[@aria-label='Select service(s) to perform actions Select Development']")
                select_environment_dev.click()
                
                edit_dev_copy = self.page.locator("//button[@aria-label='edit Development_copy']")
                edit_dev_copy.click()
 
                input_group_name = self.page.locator("//input[@value='Development_copy']")
                input_group_name.click()
                input_group_name.fill("Homologation")
 
                save_group_name = self.page.locator("//button[@aria-label='Salvar']")
                save_group_name.click()
 
                print("Ambiente HOMOLOGATION foi criado com sucesso")
                print("\n ------------------------------------------------------------ \n")
 
            elif production.is_disabled() and qtde_environments == 2:
                print(f"ATENÇÃO! Só existem 2 ambientes na sigla {sigla}. \n Você deve estimar os ambientes manualmente conforme necessário")
                print("\n ------------------------------------------------------------ \n")
 
                show_warning_message("Aviso", f"ATENÇÃO! Só existem 2 ambientes na sigla {sigla}. \n\nVocê deve estimar os ambientes manualmente conforme necessário")
 
            else:
                print("Não foi alterado nada sobre ambientes")
                print("\n ------------------------------------------------------------ \n")
        
    def shared(self, sigla):
        text_estimate = self.page.locator("//div[@data-annual-cost='true']")
        price_estimate = text_estimate.inner_text()
 
        notification = self.page.locator("//button[@aria-label='Fechar notificação']")
        if notification.is_visible():
            notification.click()
        
        shared = self.page.locator("//button[@aria-label='Compartilhar']")
        shared.click()
 
        iagree = self.page.locator("//button[@aria-label='Concordar e continuar']")
        iagree.click()
 
        self.page.wait_for_timeout(7000)
 
        copy_link = self.page.locator(".save-share-clipboard-wrapper div:first-child input").get_attribute("value")
        link = copy_link
        
        print(f"Calculadora da sigla {sigla}: " + link)
        print("\n ------------------------------------------------------------ \n")

        show_information_message_with_link("Aviso", f"Calculadora da sigla {sigla} gerada com sucesso\n\nClique no botão abaixo para copiar o link gerado\n", f"{link}")