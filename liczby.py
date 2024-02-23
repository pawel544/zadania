import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return results