# Сравним тайминг создания списка чисел Фибоначчи двумя методами: 
# метод .append()
# метод спиочного включения
#
def deco_timing(NUM_RUNS):
# декоратор тайминга
    def main_decorator(func):
        import time
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(NUM_RUNS):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
                avg_time = total / NUM_RUNS
            print("\n>>> Среднее время выполнения: %.5f секунд\n" % avg_time)
            return return_value
        return wrapper
    return main_decorator


@deco_timing(NUM_RUNS=10)
# создание списка чисел Фибоначчи методом .append()
def fibo_gen1(iters):
    fib_list = []
    for n in range(1, iters):
        fib = fibonacci(n)
        fib_list.append(fib)
    return(fib_list)

@deco_timing(NUM_RUNS=10)
# создание списка чисел Фибоначчи методом спискового включения
def fibo_gen2(iters):
    fib_list = []
    fib_list = [fibonacci(n) for n in range(1, iters)]
    return(fib_list)


def fibonacci(n):
    # вычисление ряда Фибоначчи
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



print("Список чисел Фибоначчи (метод .append()):", fibo_gen1(34))

print("Список чисел Фибоначчи (генератор списка):", fibo_gen2(34))


