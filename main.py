import csv
from typing import List


def read_csv(file_dir: str):
    with open(file_dir, newline='') as input_file:
        sensor_reader = csv.DictReader(input_file)
        dict_arr = []
        for row in sensor_reader:
            dict_arr.append(row)
    return dict_arr

def convector(data: List[str], file_dir: str):
    with open(file_dir, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Temperature_C', 'Humidity_Percent', 'Pressure_hPa', 'WindSpeed_m/s']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            temp = float(item['Temperature_F'])    #convert far to cel
            temp = (temp - 32) / 1.8

            speed = float(item['WindSpeed_mph'])
            speed = speed * 0.44704

            writer.writerow({'Timestamp': item['Timestamp'], 'Temperature_C': temp, 'Humidity_Percent': item['Humidity_Percent'],
                             'Pressure_hPa': item['Pressure_hPa'], 'WindSpeed_m/s': speed})
    return read_csv(file_dir)


if __name__ == "__main__":
    input_data = read_csv('InputFile.csv')
    convert_data = convector(input_data, 'Result.csv')