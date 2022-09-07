def majority_element_naive(elements):
    table = {}
    for e in elements:
        if e in table:
            table[e]+=1
        else:
            table[e] = 1
        if table[e] > len(elements) / 2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
