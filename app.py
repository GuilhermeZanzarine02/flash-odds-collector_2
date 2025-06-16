from config.constants import init_driver
from functions.scraper import load_page

def main():
    print('Iniciando o Diver')
    driver = init_driver()
    load_page(driver)
    input('Aperte enter para finalizar')

if __name__ == '__main__':
    main()