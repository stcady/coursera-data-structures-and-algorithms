# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_last_digit_cycle():
    F = [0 for i in range(60)]
    F[0] = 0
    F[1] = 1
    sum = 1
    curr = 1
    prev = 0
    for n in range(2, 60):
        temp = (curr+prev)%10
        prev = curr
        curr = temp
        sum += temp
        F[n] = sum%10
    return F

def fibonacci_sum(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    F = fibonacci_last_digit_cycle()
    return F[n%60]

def fibonacci_partial_sum(n, m):
    diff = fibonacci_sum(m) - fibonacci_sum(n-1)
    if diff < 0:
        return 10 + diff
    else:
        return diff

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_partial_sum(n, m))
