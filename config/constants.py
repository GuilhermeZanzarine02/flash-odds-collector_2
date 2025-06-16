""" Constantes como URL, driver, dados etc."""

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

def get_default_edge_options():

    """
    Define e retorna as opções padrão para o navegador Microsoft Edge,
    permitindo configurar argumentos que controlam o comportamento do navegador,
    como segurança, performance e execução em segundo plano (headless).
    """
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox") 
    return options


def init_driver():
    """
    Inicializa o navegador e acessa a URL do site desejado, preparando o ambiente para automação ou testes. 
    """
    options = get_default_edge_options()
    service = EdgeService(executable_path=r"C:\Users\zanza\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    return driver