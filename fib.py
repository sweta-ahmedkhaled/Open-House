import sys
import time

from fibonacii_naieve import fib_naive
from fibonacii_fast import fib_array


def main():
    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <n> <naive|fast>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: n must be an integer.")
        sys.exit(1)

    method = sys.argv[2].lower()

    # Select function
    if method == "naive":
        function = fib_naive
    elif method == "fast":
        function = fib_array
    else:
        print("Error: method must be 'naive' or 'fast'.")
        sys.exit(1)

    # Measure execution time
    start = time.time()
    result = function(n)
    elapsed_time = time.time() - start

    # Display results
    print(f"fib({n}) = {result}")
    print(f"{method:>6} : {elapsed_time:.6f}s")


if __name__ == "__main__":
    main()