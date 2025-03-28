import csv


def read_csv(file_dir: str):
    with open(file_dir, newline='') as input_file:
        sensor_reader = csv.DictReader(input_file)
        dict_arr = []
        for row in sensor_reader:
            dict_arr.append(row)
    return dict_arr
