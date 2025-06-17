import pandas as pd
import numpy as np
from datetime import datetime
from src.data_cleaning import data_cleaning

def convert_to_csv(matchup, location, fixture_datetime, bookmaker, odds_list):
    now = datetime.now().strftime(r"%Y%m%d_%H%M%S")

    #Local e capacidade
    stadiums = location[::2]
    capacities = [int(c.replace(" ", "")) for c in location[1::2]]

    #Data e Hora
    datas, horas = data_cleaning(fixture_datetime)

    #Odds
    home_odds = [float(odds_list[i]) for i in range(0, len(odds_list), 3)]
    draw_odds = [float(odds_list[i]) for i in range(1, len(odds_list), 3)]
    away_odds = [float(odds_list[i]) for i in range(2, len(odds_list), 3)]
    
    df = pd.DataFrame({
        'Matchup' : matchup,
        'Stadium' : stadiums,
        'Capacity' : capacities,
        'Data' : datas,
        'Horario' : horas,
        'Bookmaker' : bookmaker,
        'Home_Odd' : home_odds,
        'Draw_Odd' : draw_odds,
        'Away_Odd' : away_odds
    })

    df_odds = pd.DataFrame({
        'Home_Odd' : home_odds,
        'Draw_Odd' : draw_odds,
        'Away_Odd' : away_odds
    })

    file_name = fr'C:\Users\zanza\Desktop\flash-odds-collector_2\flash-odds-collector_2\data\dados_flashscore{now}'
    file_name_odd = fr'C:\Users\zanza\Desktop\flash-odds-collector_2\flash-odds-collector_2\data\odds_flashscore{now}'


    df.to_csv(file_name, index=False)
    df_odds.to_csv(file_name_odd, index=False)

