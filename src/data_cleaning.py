def data_cleaning(list):
    datas = []
    horas = []

    for item in list:
        data, hora = item.split()
        datas.append(data)
        horas.append(hora)
        
    return datas, horas
