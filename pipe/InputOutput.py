from typing import List, Dict
import csv

def read_csv(file_dir: str):
    with open(file_dir, newline='') as input_file:
        sensor_reader = csv.DictReader(input_file)
        dict_arr = []
        for row in sensor_reader:
            dict_arr.append(row)
    return dict_arr

def write_csv(file_dir: str, data: List[Dict[str, float]]):
    with open(file_dir, 'w', newline='') as csvfile:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(data)):
            writer.writerow(data[i])
