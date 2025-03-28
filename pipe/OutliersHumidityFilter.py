from typing import List, Dict

def outliers_humidity_filter(data: List[Dict[str, float]]):
    anomaly_data = []
    normal_data = []
    for i in range(len(data)):
        if not (30 <= data[i]['Humidity_Percent'] <= 90):
            anomaly_data.append(data[i])
        else:
            normal_data.append(data[i])

    return normal_data, anomaly_data