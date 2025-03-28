from typing import List, Dict

def low_temperature_filter(data: List[Dict[str, float]]):
    anomaly_data = []
    normal_data = []
    for i in range(len(data)):
        if data[i]['Temperature_C'] >= 10:
            normal_data.append(data[i])
        else:
            anomaly_data.append(data[i])

    return normal_data, anomaly_data