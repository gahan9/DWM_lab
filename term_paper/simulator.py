import os
import geohash

datasets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'datasets'))
dataset_files = [os.path.join(datasets_dir, file) for file in os.listdir(datasets_dir)]


def parseline(line):
    if line[-1] == '\n':
        line = line[:-1]
    client_name, timestamp, latitude, longitude = line.split(',')
    latitude, longitude = float(latitude), float(longitude)
    gh = geohash.encode(latitude, longitude, precision=10)
    return {
        'client': client_name,
        'geohash': gh,
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    }


def nextline(dataset_file):
    client_name = dataset_file.split('.')[0]
    client_name = client_name.split('/')[-1]
    with open(dataset_file, mode='r') as fp:
        for line in fp.readlines():
            yield parseline(line)
    yield None


def get_random_data():
    file_pointers = [nextline(dataset_file) for dataset_file in dataset_files]
    while len(file_pointers) > 0:
        for fp in file_pointers:
            line = fp.__next__()
            if line is None:
                file_pointers.remove(fp)
            else:
                # print(line)
                yield line


def get_sequential_data():
    file_pointers = [nextline(dataset_file) for dataset_file in dataset_files]
    for fp in file_pointers:
        line = fp.__next__()
        while line is not None:
            yield line
            line = fp.__next__()
