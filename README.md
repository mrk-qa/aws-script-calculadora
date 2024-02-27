# Calculadora AWS - NTT DATA
 
<h1 align="left">
    <img width="300px" src="./assets/ntt_logo.png" alt="ntt-data-logo">
</h1>
 
O script realiza o processo hoje feito de forma manual para gerar a calculadora v0, que é:
 
### Descrição das etapas do script
 
- Valida as informações por sigla na planilha CMDB, como: ambientes, quantidade de servidores, sistema operacional, vCPU, memória RAM, armazenamento, tipo de aplicação (servidor ou banco de dados) e etc
- Gera o template de uma sigla no excel para upload na AWS
- Pega as recomendações das instâncias na região de São Paulo via API da AWS
- Acessa a URL calculadora AWS
- Faz o upload do template excel
- Valida se existe EC2 sendo webservers e adiciona ALB com a quantidade de webservers de cada ambiente
- Estima o ambiente que estiver faltando conforme necessário: dev ou homol (se estiver faltando)
- E por fim, exporta o link da calculadora pronta
 
------
 
# Setup e Instalação
 
- Instalar o Python => 3.9.5 e configurar o arquivo .pip
- Variáveis de ambiente
- Após todas as configurações, confirmar se o Python está instalado rodando o comando: `python --version`
- Instalar as libs rodando o comando: `pip install -r requirements.txt`
- Finalizar instalação do playwright incluindo navegadores rodando o comando: `playwright install`
 
# Comandos
 
- Para pegar as recomendações das instâncias na região de São Paulo via API da AWS, rodar o comando: `python data/servers/get_instances.py`
- Para rodar o script e gerar a calculadora: `pytest --headed -s`
 
------
 
*Develop by: Anderson e Marco*