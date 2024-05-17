import time
import multiprocessing

def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def factorize_sync(*numbers):
    return [factors(number) for number in numbers]

def factorize_parallel(*numbers):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(factors, numbers)
    return result

if __name__ == '__main__':
    # Тестування правильності функції
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    # Вимірювання часу виконання для синхронної реалізації
    start_time = time.time()
    factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Синхронна реалізація: {end_time - start_time} секунд")

    # Вимірювання часу виконання для паралельної реалізації
    start_time = time.time()
    factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Паралельна реалізація: {end_time - start_time} секунд")
