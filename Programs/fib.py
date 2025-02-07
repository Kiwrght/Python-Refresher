from functools import lru_cache, wraps
import time
import matplotlib.pyplot as plt

# x and y coordinates on graph
x = []
y = []


# Plotting fibonacci numbers and calculating how long it takes to calculate each one
def timer(fib):
    @wraps(fib)
    def timerWrapper(n):

        # Times and stores the fibonacci number and time
        begin = time.perf_counter()  # begins the timer
        result = fib(n)  # calculates the fibonacci number
        end = time.perf_counter()  # ends timer
        total_time = end - begin  # calculates the total calculation time

        # adds the time and number values
        x.append(n)
        y.append(total_time)

        # prints the amount of time it took to calculate and the resulting value for each number
        print("Finished in: ", total_time, "s f(", n, ") -> ", result)
        return result

    return timerWrapper


@lru_cache(maxsize=128)
@timer
def fib(n: int) -> int:
    """Calculating the nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ##returning a none type Question ##
        return fib(n - 1) + fib(n - 2)  # returns the calculated fibonacci number


if __name__ == "__main__":
    fib(100)
    # Plotting the time it takes to calculate the fibonacci number
    plt.plot(x, y, label="Time taken to compute Fibonacci")
    plt.title("Fibonacci Calculation Time vs Fibonacci Index")
    plt.grid(True)
    plt.show()
