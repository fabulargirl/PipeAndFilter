from typing import List, Dict


def temperature_convector(data: List[Dict[str: str]]):
    for i in range(len(data)):
        data[i]['Temperature_F'] = (float(data[i]['Temperature_F']) - 32) / 1.8

    return data


def speed_convector(data: List[Dict[str: str]]):
    for i in range(len(data)):
        data[i]['WindSpeed_mph'] = float(data[i]['WindSpeed_mph']) * 0.44704

    return data
