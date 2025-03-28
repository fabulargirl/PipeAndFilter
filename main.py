from pipe.InputOutput import *
from pipe.convectors import *
from pipe.pressureFilters import *
from pipe.LowTempFilter import *
from pipe.OutliersHumidityFilter import *


def PipeAndFilter():
    data = read_csv('InputFile.csv')
    data = str2float(data)
    data = temperature_convector(data)
    data = speed_convector(data)

    mark_wild_pressure, wild_pressure = invalid_pressure_filter(data)
    write_csv('Pressure.csv', wild_pressure)
    data = interpolation(data, mark_wild_pressure)

    normal_data, anomaly_temp_data = low_temperature_filter(data)
    write_csv('Temperature.csv',anomaly_temp_data)

    data, anomaly_temp_data = outliers_humidity_filter(data)
    write_csv('Humidity.csv', anomaly_temp_data)

    data, anomaly_temp_data = low_temperature_filter(data)
    write_csv('Result.csv', data)

    return 0


if __name__ == "__main__":
    PipeAndFilter()