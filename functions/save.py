import pandas as pd
from datetime import datetime
from src.data_cleaning import data_cleaning

def convert_to_csv(matchup, location, fixture_datetime):
    now = datetime.now().strftime(r"%Y%m%d_%H%M%S")

    #Local e capacidade
    stadiums = location[::2]
    capacities = [int(c.replace(" ", "")) for c in location[1::2]]

    #Data e Hora
    datas, horas = data_cleaning(fixture_datetime)
    
    df = pd.DataFrame({
        'Matchup' : matchup,
        'Stadium' : stadiums,
        'Capacity' : capacities,
        'Data' : datas,
        'Horario' : horas
    })

    file_name = fr'C:\Users\zanza\Desktop\flash-odds-collector_2\flash-odds-collector_2\data\dados_flashscore{now}'

    df.to_csv(file_name, index=False)

