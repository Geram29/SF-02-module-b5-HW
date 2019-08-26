def deco_timing(NUM_RUNS):
    def main_decorator(func):
        import time
        def wrapper():
            total = 0
            for i in range(NUM_RUNS):
                start = time.time()
                return_value = func()
                end = time.time()
                total = total + (end-start)
                avg_time = total / NUM_RUNS
            print("\n>>> Среднее время выполнения: %.5f секунд\n" % avg_time)
            return return_value
        return wrapper
    return main_decorator


@deco_timing(NUM_RUNS=10)
def fibo_gen():
    fib_list = []
    for n in range(1, 50):
        fib = fibonacci(n)
        if fib >= 6000000:
            break
        fib_list.append(fib)
    return(fib_list)

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



print("Список чисел Фибоначчи:", fibo_gen())


