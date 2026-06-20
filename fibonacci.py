import time

# ── Naive Recursive Fibonacci ──────────────────────────────────────────────────
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ── Array-based Fibonacci ──────────────────────────────────────────────────────
def fib_array(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ── Demo ───────────────────────────────────────────────────────────────────────
n = 35

start = time.time()
result_naive = fib_naive(n)
naive_time = time.time() - start

start = time.time()
result_array = fib_array(n)
array_time = time.time() - start

print(f"fib({n}) = {result_naive}")
print(f"  Naive  : {naive_time:.4f}s")
print(f"  Array  : {array_time:.6f}s")
print(f"  Speedup: {naive_time / array_time:.0f}x faster")
