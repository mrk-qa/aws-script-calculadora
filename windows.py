from cx_Freeze import setup, Executable
import os

ntt_icon = os.getcwd() + "/assets/ntt_icone.ico"

# Lista de módulos a serem excluídos do executável
excludes = [
    "tkinter",
    "distutils",
    "email",
    "html",
    "http",
    "numpy",
    "pytz",
    "json",
    "async_generator",
    "markupsafe",
    "jinja2",
    "asyncio",
    "collections",
    "greenlet",
    "importlib",
    "logging",
    "outcome",
    "pyperclip",
    "pyrect",
    "pyscreeze",
    "pytweening",
    "setuptools",
    "sniffio",
    "sortedcontainers",
    "trio",
    "unittest"
]

# Lista de módulos a serem incluídos no executável
packages = [
    "data",
    "pages",
]

# Lista de arquivos a serem incluídos no executável
include_files = [
    ("assets", "assets"),
    ("browser", "browser"),
    ("data", "data"),
    ("siglas", "siglas"),
    ("pages", "pages"),
    ("calculadora.py", "calculadora.py"),
]

# Configuração do executável
setup(
    name="Script Calculadora AWS - NTT DATA",
    version="1.0",
    description="Automação de tarefas para gerar uma calculadora AWS",
    executables=[Executable("calculadora.py", icon=ntt_icon)],
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files,
            "excludes": excludes,
        }
    }
)
