import numpy as np
import time as t


def naive(filename):    # Naive algorithm
    data = np.memmap(filename, dtype='uint8')
    n = 0
    Sum = 0
    SumSq = 0
    for x in data:      # execute 1 billion times to update the corresponding value
        x = float(x)
        n += 1
        Sum += x
        SumSq += x * x
    mean = Sum / n
    variance = (SumSq - (Sum * Sum) / n) / n
    del data    # free the memory
    return mean, variance


def update(existingAggregate, newValue):    # Welford's algorithm
    (count, mean, M2) = existingAggregate
    count += 1
    delta_1 = newValue - mean   # delta_1 is computed with the old mean
    mean += delta_1 / count     # new mean is calculated
    delta_2 = newValue - mean   # delta_2 is computed with the new mean
    M2 += delta_1 * delta_2     # calculate M2
    return count, mean, M2


def finalize(existingAggregate):    # Welford's algorithm
    (count, mean, M2) = existingAggregate
    (mean, variance) = (mean, M2 / count)
    return mean, variance


def welford(filename):
    data = np.memmap(filename, dtype='uint8')
    aggregate = (0, 0, 0)
    for x in data:      # execute 1 billion times to update the corresponding value
        x = float(x)
        aggregate = update(aggregate, x)
    result = finalize(aggregate)
    del data    # free the memory
    return result


def onepass(filename):  # One-pass arbitrary order method
    data = np.memmap(filename, dtype='uint8')
    n = 0
    mean = 0
    cs2 = 0
    # below algebra are all the same as the given attachment
    for x in data:
        x = float(x)
        n += 1
        delta = x - mean
        mean = mean + delta / n
        cs2 = cs2 + (delta * delta * (n-1)) / n     # given formula

    del data    # free the memory
    return mean, cs2 / n    # variance = cs2/n


def histogram(filename):
    data = np.memmap(filename, dtype='uint8')
    n = len(data)   # n: 1000000000
    hist = np.bincount(data)    # count number of occurrences of each value in the array

    sum_trunk = np.sum(np.arange(len(hist)) * hist)             # sum up the area of all trunks
    sum_trunk_squared = np.sum(np.arange(len(hist))**2 * hist)  # sum up the bin square times trunk

    mean = sum_trunk / n
    variance = (sum_trunk_squared - n * mean * mean) / n
    del data    # free the memory
    return mean, variance


if __name__ == '__main__':
    filename = "measurement_data_2023_uint8.bin"

    print("----------Naive algorithm----------")
    start_time = t.time()
    naive_mean, naive_var = naive(filename)
    print("Mean: ", naive_mean)
    print("Var: ", naive_var)
    end_time = t.time()
    print("Time: ", end_time - start_time)

    print("----------Welford's algorithm----------")
    start_time = t.time()
    welf_mean, welf_var = welford(filename)
    print("Mean: ", welf_mean)
    print("Variance: ", welf_var)
    end_time = t.time()
    print("Time: ", end_time - start_time)

    print("----------One pass----------")
    start_time = t.time()
    onep_mean, onep_var = onepass(filename)
    print("Mean: ", onep_mean)
    print("Variance: ", onep_var)
    end_time = t.time()
    print("Time: ", end_time - start_time)

    print("----------Histogram method----------")
    start_time = t.time()
    hist_mean, hist_var = histogram(filename)
    print("Mean: ", hist_mean)
    print("Variance: ", hist_var)
    end_time = t.time()
    print("Time: ", end_time - start_time)
