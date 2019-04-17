import os
import geohash

datasets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'datasets'))
dataset_files = [os.path.join(datasets_dir, file) for file in os.listdir(datasets_dir)]


def parseline(line, precision=5):
    if line[-1] == '\n':
        line = line[:-1]
    taxi_id, timestamp, latitude, longitude = line.split(',')
    latitude, longitude = float(latitude), float(longitude)
    gh = geohash.encode(latitude, longitude, precision=precision)
    return {
        'taxi_id': taxi_id,
        'geohash': gh,
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    }


def nextline(dataset_file, precision):
    taxi_id = dataset_file.split('.')[0]
    taxi_id = taxi_id.split('/')[-1]
    with open(dataset_file, mode='r') as fp:
        for line in fp.readlines():
            yield parseline(line, precision)
    yield None


def get_random_data(precision):
    file_pointers = [nextline(dataset_file, precision) for dataset_file in dataset_files]
    while len(file_pointers) > 0:
        for fp in file_pointers:
            line = fp.__next__()
            if line is None:
                file_pointers.remove(fp)
            else:
                # print(line)
                yield line


def get_sequential_data(precision):
    file_pointers = [nextline(dataset_file, precision) for dataset_file in dataset_files]
    for fp in file_pointers:
        line = fp.__next__()
        while line is not None:
            yield line
            line = fp.__next__()

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()