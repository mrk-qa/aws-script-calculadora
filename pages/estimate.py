from playwright.sync_api import Page
from playwright.sync_api import expect

class EstimatePage:
    def __init__(self, page: Page):
        self.page = page

    def view_page_estimate(self):
        my_estimate = self.page.locator("//h1")
        expect(my_estimate).to_have_text("My Estimate")
 
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
                environment.click()
            
                resources = self.page.query_selector_all("//tr[@data-selection-item='item']")
                qtde_resources = len(resources)
                
                r = 1
                while r <= qtde_resources:
                    each_edits = self.page.locator(f"tr[data-selection-item='item']:nth-child({r}) :nth-child(2) [data-cy='edit-service']").all()

                    for edit in each_edits:
                        
                        print(f"Editando EC2 {r} para editar no ambiente {environment_name} \n")

                        edit.click(timeout=80000)

                        find = self.page.locator("//div[@class='show']/span[4]/div/div")
                        find.click(timeout=80000)

                        check = self.page.locator("//input[@aria-label='Enable monitoring']/..")
                        check.click(timeout=80000)

                        update = self.page.locator("//button[@aria-label='Atualizar']")
                        update.click(timeout=80000)

                    r += 1

                print("\n ------------------------------------------------------------ \n")

            e += 1

    def resources_alb(self):
        environments = self.page.query_selector_all("li [data-parent-group='true'] p")
        qtde_environments = len(environments)

        e = 1
        while e <= qtde_environments:
            each_environment = self.page.locator(f"li [data-parent-group='true']:nth-child({e}) p").all()

            for environment in each_environment:
                print(f"Acessando ambiente {e}:  para validar as EC2")
                environment.click()

                resources = self.page.query_selector_all("//tr[@data-selection-item='item']")
                qtde_resources = len(resources)

                w = 1
                while w <= qtde_resources:
                    each_webservers = self.page.locator(f"tr[data-selection-item='item']:nth-child({w}) :nth-child(6) span button span p").all()

                    for webserver in each_webservers:
                        describe_server = webserver.inner_text()

                        if "WEB SERVERS" in describe_server:
                            count_webservers = describe_server.count("WEB SERVERS")
                            print(f"\n Foi identificado que o ambiente  possui {count_webservers} EC2 sendo WEB SERVERS \n")
                            
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

                            self.page.wait_for_timeout(4000)

                            save_and_view_resume = self.page.locator("//button[@aria-label='Salvar e visualizar resumo']")
                            save_and_view_resume.click()

                            print("Recurso: Elastic Load Balacing foi adicionado com sucesso \n")
                            print(f"Incluindo {count_webservers} a quantidade de ALB")

                    w += 1

                print("\n ------------------------------------------------------------ \n")

            e += 1

    def environments(self, sigla):
        sigla_envionments = self.page.locator(f"//li//p[contains(text(), '{sigla}')]")
        sigla_envionments.click()

        select_environment = self.page.query_selector_all("tr[data-selection-item='item'] button strong")
        qtde_environments = len(select_environment)
        environment_name = select_environment[0].inner_text()

        print ("Validando os ambientes \n")

        if qtde_environments == 3:
            print("Já existem 3 ambientes estimados")
            print("\n ------------------------------------------------------------ \n")
        
        elif qtde_environments == 1:
            print(f"ATENÇÃO! Só existe o ambiente {environment_name}, estimar os ambientes manualmente conforme necessário")
            print("\n ------------------------------------------------------------ \n")

        elif "Homologation" in environment_name:
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

        elif "Development" in environment_name:
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

        else:
            print("Erro ao validar os ambientes")
            print("\n ------------------------------------------------------------ \n")
        
    def shared(self, sigla):
        shared = self.page.locator("//button[@aria-label='Compartilhar']")
        shared.click()

        iagree = self.page.locator("//button[@aria-label='Concordar e continuar']")
        iagree.click()

        self.page.wait_for_timeout(5000)

        copy_link = self.page.locator(".save-share-clipboard-wrapper div:first-child input").get_attribute("value")
        link = copy_link
        print(f"Calculadora da sigla {sigla}: " + link + " \n")

        with open(f"url/url_{sigla}.txt", "w") as f:
            f.write(link)

        print("\n ------------------------------------------------------------ \n")

        self.page.screenshot(path=f"reports/calculadora_{sigla}.png", full_page=True)
        
    def update_estimate(self):
        update = self.page.locator("//button[@aria-label='Botão Atualizar estimativa']")
        update.click()

        print("Iniciando atualização de estimativa")
        print("\n ------------------------------------------------------------ \n")