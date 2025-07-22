def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    product = max_pairwise_product_naive(numbers)
    print(product)
