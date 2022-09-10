import math

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(M, m, i, j, ops):
    minimum = math.inf
    maximum = -math.inf
    for k in range(i, j):
        maxmax = evaluate(M[i][k], M[k+1][j], ops[k])
        maxmin = evaluate(M[i][k], m[k+1][j], ops[k])
        minmax = evaluate(m[i][k], M[k+1][j], ops[k])
        minmin = evaluate(m[i][k], m[k+1][j], ops[k])
        minimum = min(minimum, maxmax, maxmin, minmax, minmin)
        maximum = max(maximum, maxmax, maxmin, minmax, minmin)
    return minimum, maximum

def maximum_value(dataset):
    OPSYMS = ['*', '+', '-']
    ops = []
    nums = []
    for char in dataset:
        if char in OPSYMS:
            ops.append(char)
        else:
            nums.append(int(char))
    mins = [[None for x in range(len(nums))] for x in range(len(nums))]
    maxes = [[None for x in range(len(nums))] for x in range(len(nums))]
    for i in range(len(nums)):
        mins[i][i] = nums[i]
        maxes[i][i] = nums[i]
    for s in range(1, len(nums)):
        for i in range(0, len(nums)-s):
            j = i + s
            mins[i][j], maxes[i][j] = min_and_max(maxes, mins, i, j, ops)
    return maxes[0][len(nums)-1]

if __name__ == "__main__":
    print(maximum_value(input()))
