from typing import List, Dict


def invalid_pressure_filter(data: List[Dict[str, float]]):
    mark_wild_pressure = list()
    wild_pressure = list()
    for i in range(1, len(data) - 1):
        if abs(data[i]['Pressure_hPa'] - data[i - 1]['Pressure_hPa']) > 10 and abs(data[i]['Pressure_hPa'] -
                                                                                   data[i + 1]['Pressure_hPa']) > 10:
            mark_wild_pressure.append(i)
            wild_pressure.append(data[i])

    return mark_wild_pressure, wild_pressure


def interpolation(data: List[Dict[str, float]], mark_pressure: List[int]):
    while len(mark_pressure):
        item = mark_pressure.pop(0)
        left_index = item - 1
        right_index = item + 1

        while left_index in mark_pressure and left_index >= 0:
            left_index -= 1

        while right_index in mark_pressure and left_index >= len(data):
            right_index += 1

        slope = abs(data[right_index]['Pressure_hPa'] - data[left_index]['Pressure_hPa']) / (right_index - left_index)

        if data[left_index]['Pressure_hPa'] < data[right_index]['Pressure_hPa']:
            data[item]['Pressure_hPa'] = data[left_index]['Pressure_hPa'] + slope * (item - left_index)
        else:
            data[item]['Pressure_hPa'] = data[left_index]['Pressure_hPa'] - slope * (item - left_index)

    return data
