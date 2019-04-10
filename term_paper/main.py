import simulator
import itertools
from datetime import datetime

def generate_file_1():
    with open('file1.txt', 'w') as fp:
        for df in simulator.get_sequential_data():
            fp.write("{}, {}, {}, {}\n".format(
                df['client'], df['latitude'], df['longitude'], df['timestamp']))

def generate_file_2():
    with open('file2.txt', 'w') as fp:
        for df in simulator.get_sequential_data():
            fp.write("{}, {}, {}\n".format(
                df['client'], df['geohash'], df['timestamp']))


def parseline(line):
    if line[-1] == '\n':
        line = line[:-1]
    client_name, geohash, timestamp = line.split(',')
    epoch_time = datetime.strptime(timestamp, ' %Y-%m-%d %H:%M:%S').timestamp()
    return geohash, epoch_time

def generate_file_3():
    with open('file3.txt', 'w') as write_file:
        with open('file2.txt', 'r') as file1:
            for file1_line in file1.readlines():
                dataset1 = parseline(file1_line)
                with open('file2.txt', 'r') as file2:
                    for file2_line in file2.readlines():
                        dataset2 = parseline(file2_line)
                        write_file.write("{}, {}, {}\n".format(
                             dataset1[0], dataset2[0], dataset1[1] - dataset2[1]))


if __name__ == '__main__':
    generate_file_1()
    generate_file_2()
    generate_file_3()
