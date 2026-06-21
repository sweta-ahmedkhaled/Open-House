# ── Naive Recursive Fibonacci ──────────────────────────────────────────────────
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)