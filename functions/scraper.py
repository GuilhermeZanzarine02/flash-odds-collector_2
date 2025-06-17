from selenium.webdriver.common.by import By
from functions.navigation import accept_cookies, open_match_details
from functions.save import convert_to_csv

def load_page(driver):
    country = 'brasil'

    league = 'brasileirao-betano'

    url_base = f'https://www.flashscore.com.br/futebol/{country}/{league}/'

    driver.get(url_base)
    driver.maximize_window()

    accept_cookies(driver)
    matchup, location, fixture_datetime, bookmaker, odds_list = open_match_details(driver)
    convert_to_csv(matchup, location, fixture_datetime, bookmaker, odds_list)