def fibonacci_number(n):
    a = [0, 1]
    if n <= 1:
        return a[n]
    for i in range(2, n + 1):
        next = a[i - 2] + a[i - 1]
        a.append(next)
    return a[-1]


if __name__ == "__main__":
    n = int(input())
    fib = fibonacci_number(n)
    print(fib)
