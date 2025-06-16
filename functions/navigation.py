from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def accept_cookies(driver):

    cookies = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, 'onetrust-accept-btn-handler')
        )
    )

    cookies.click()

def open_match_details(driver):

    try:
        events = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'eventRowLink')
            )
        )

        links = [event.get_attribute('href') for event in events if event.get_attribute('href')][:10]

        matchup = []
        unique = []
        stadiums = []
        fixture_datetime = []
        seen = set()

        for link in links:
            driver.get(link)
            participants = get_participant_name(driver)
            date_time = get_date_time(driver)
            locations =  get_location(driver)

            for participant in participants:
                name = participant.text.strip()
                if name and name not in seen:
                    unique.append(name)
                    seen.add(name)

            for location in locations:
                location_name = location.text.strip()
                stadiums.append(location_name)
            
            dt = date_time.text.strip()
            fixture_datetime.append(dt)
                
        for i in range(0, len(unique), 2):
            try:
                home = unique[i]
                away = unique[i + 1]
                fixture = f'{home} x {away}'
                matchup.append(fixture)

            except IndexError:
                print(f'Item faltando para formar confronto em índice {i}')

        return matchup, stadiums, fixture_datetime
    
    except Exception as e:
        print(f'Erro ao obter link dos eventos: {e}')

def get_participant_name(driver):
    
    try:
        participant_name = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.participant__participantName.participant__overflow')
            )
        )

        return participant_name

    except Exception as e:
        print(f'Erro ao encontrar nomes dos participantes: {e}')

def get_location(driver):

    locations = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.wcl-simpleText_Asp-0.wcl-scores-simpleText-01_pV2Wk.wcl-bold_roH-0')
        )
    )

    return locations

def get_date_time(driver):
    date_time = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="detail"]/div[3]/div[1]/div[1]/div')
        )
    )
    return date_time