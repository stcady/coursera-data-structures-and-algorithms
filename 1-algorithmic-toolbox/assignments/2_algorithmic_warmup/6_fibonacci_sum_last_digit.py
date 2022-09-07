def naive_fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

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
    if n < 0:
        raise Exception("Invalid input. Must be non-negative number.")
    F = fibonacci_last_digit_cycle()
    return F[n%60]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
