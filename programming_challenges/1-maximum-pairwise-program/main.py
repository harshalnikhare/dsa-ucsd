def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product


# Faster Algorithm
def max_pairwise_product_trivial(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(1, n):
        if numbers[index1] < numbers[i]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(1, n):
        if numbers[index1] != numbers[i] and numbers[index2] < numbers[i]:
            index2 = i

    return numbers[index1] * numbers[index2]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    product = max_pairwise_product_trivial(numbers)
    print(product)
