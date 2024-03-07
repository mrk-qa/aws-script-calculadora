from cx_Freeze import setup, Executable
import os
import pyautogui
import subprocess
import time

############################################################
############## EXPORTAÇÃO DE DADOS DO BROWSER ##############
############################################################

# Verificar se existe a pasta browser
if not os.path.exists("browser"):
    # Nome do arquivo autoextraível
    arquivo_autoextraivel = "browser.exe"

    # Executar o arquivo autoextraível
    processo = subprocess.Popen(arquivo_autoextraivel)

    # Esperar um segundo para garantir que a janela apareça
    time.sleep(1)

    # Clicar diretamente no botão "Extract"
    pyautogui.press('enter')

    # Minimizar a janela ativa usando a combinação de teclas Win + ↓
    pyautogui.hotkey('win', 'down')
    
    # Esperar até que o processo de descompactação termine
    processo.wait()

############################################################
################## CRIAÇAO DO EXECUTÁVEL ###################
############################################################

excludes = [
    "tkinter",
    "email",
    "tk8.6",
    "unittest"
]

include_files = [
    ("assets", "assets"),
    ("browser", "browser"),
    ("data", "data"),
    ("siglas", "siglas"),
    ("pages", "pages"),
    ("dados_servidores_teste.xlsx", "dados_servidores_teste.xlsx"),
    ("calculadora.py", "calculadora.py"),
]

ntt_icon = os.getcwd() + "/assets/ntt_icone.ico"

# Configuração do executável
setup(
    name="Script Calculadora AWS",
    version="1.0",
    description="Automação de tarefas para gerar uma calculadora AWS",
    executables=[Executable("calculadora.py", base="Win32GUI", icon=ntt_icon, target_name="Script Calculadora AWS.exe")],
    options={
        "build_exe": {
            "include_files": include_files,
            "excludes": excludes
        }
    }
)