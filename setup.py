from cx_Freeze import setup, Executable
import os

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