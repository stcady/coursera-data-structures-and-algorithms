from itertools import permutations
from operator import truediv


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def is_better(num1, num2):
    if num1+num2 > num2+num1:
        return True
    return False

def largest_number(numbers):
    output = ""
    while len(numbers) > 0:
        max = '0'
        for number in numbers:
            if is_better(number, max):
                max = number
        output += max
        numbers.remove(max)
    return output


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
