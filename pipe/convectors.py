from typing import List, Dict

def str2float(data):
    for i in range(len(data)):
        data[i]['Temperature_F'] = float(data[i]['Temperature_F'])
        data[i]['Humidity_Percent'] = float(data[i]['Humidity_Percent'])
        data[i]['Pressure_hPa'] = float(data[i]['Pressure_hPa'])
        data[i]['WindSpeed_mph'] = float(data[i]['WindSpeed_mph'])

    return data

def temperature_convector(data: List[Dict[str, float]]):
    for i in range(len(data)):
        data[i]['Temperature_C'] = (data[i]['Temperature_F'] - 32) / 1.8
        del data[i]['Temperature_F']

    return data

def speed_convector(data: List[Dict[str, float]]):
    for i in range(len(data)):
        data[i]['WindSpeed_ms'] =  data[i]['WindSpeed_mph'] * 0.44704
        del data[i]['WindSpeed_mph']

    return data