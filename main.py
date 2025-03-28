from pipe.InputOutput import read_csv
from pipe.convectors import str2float
from pipe.pressureFilters import invalid_pressure_filter, interpolation


def main():
    data = read_csv('inputFile.csv')
    data = str2float(data)
    mark_wild_pressure, wild_pressure = invalid_pressure_filter(data)
    data = interpolation(data, mark_wild_pressure)

    mark_wild_pressure, wild_pressure = invalid_pressure_filter(data)

    print(mark_wild_pressure)

    for i in range(len(data)):
        print(data[i])


if __name__ == "__main__":
    main()