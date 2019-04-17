import os
import simulator
import itertools
from time import sleep
from datetime import datetime

PRECISION = 5

def generate_file_1():
    with open('file1.txt', 'w') as fp:
        for df in simulator.get_sequential_data(precision=PRECISION):
            fp.write("{}, {}, {}, {}\n".format(
                df['taxi_id'], df['latitude'], df['longitude'], df['timestamp']))

def generate_file_2():
    with open('file2.txt', 'w') as fp:
        for df in simulator.get_sequential_data(precision=PRECISION):
            fp.write("{}, {}, {}\n".format(
                df['taxi_id'], df['geohash'], df['timestamp']))


def parseline(line):
    if line[-1] == '\n':
        line = line[:-1]
    taxi_id, geohash, timestamp = line.split(',')
    epoch_time = datetime.strptime(timestamp, ' %Y-%m-%d %H:%M:%S').timestamp()
    return geohash, epoch_time, taxi_id

def generate_file_3(prevent_skip=False):
    records_to_process = int(os.popen("wc -l file2.txt").read().strip().split()[0])
    print("Processing Dissimilarity computation for {} records..".format(records_to_process))
    # Initial call to print 0% progress
    simulator.printProgressBar(0, records_to_process-1, prefix = 'Progress:', suffix = 'Complete', length = 50)
    with open('file3.txt', 'w') as write_file:
        skip_n = 0
        with open('file2.txt', 'r') as file1:
            count = 0
            for file1_line in file1.readlines():
                skip_n += 1
                count += 1
                dataset1 = parseline(file1_line)
                simulator.printProgressBar(count, records_to_process, prefix = 'Progress:', suffix = 'Complete', length = 50)
                with open('file2.txt', 'r') as file2:
                    line_no = 0
                    for file2_line in file2.readlines():
                        line_no += 1
                        if line_no > skip_n or prevent_skip:
                            dataset2 = parseline(file2_line)
                            if dataset1[2] == dataset1[2] and dataset1 != dataset2 and dataset1[0] != dataset2[0]:
                                cmp_str = "{}-{}".format(dataset1[2], dataset2[2])
                                write_file.write("{}, {}, {}, {} \n".format(cmp_str, dataset1[0], dataset2[0], dataset1[1] - dataset2[1]))


if __name__ == '__main__':
    generate_file_1()
    generate_file_2()
    generate_file_3()