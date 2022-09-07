def edit_distance(first_string, second_string):
    first_length = len(first_string)
    second_length = len(second_string)
    result = [[0 for x in range(second_length + 1)] for x in range(first_length + 1)]
    for i in range(first_length + 1):
        for j in range(second_length + 1):
            if i == 0:
                result[i][j] = j
            elif j == 0:
                result[i][j] = i
            elif first_string[i-1] == second_string[j-1]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = 1 + min(result[i][j-1], result[i-1][j], result[i-1][j-1])
    return result[first_length][second_length]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
