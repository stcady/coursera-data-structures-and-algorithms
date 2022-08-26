
def max_pairwise_product(numbers):
    length = len(numbers)
    max1 = -1
    max1_index = -1
    max2 = -1
    if length < 2:
        raise Exception("Invalid length. Length must be greater than 1.")
    for i in range(length):
        if numbers[i] < 0:
            raise Exception("Numbers in array must be positive numbers.")
        if numbers[i] > max1:
            max1_index = i
            max1 = numbers[i]
    for j in range(length):
        if j != max1_index and numbers[j] > max2:
            max2 = numbers[j]
    return max1*max2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))