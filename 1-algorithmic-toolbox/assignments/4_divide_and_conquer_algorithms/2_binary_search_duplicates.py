def binary_search(keys, query):
    return first_occurance(keys, 0, len(keys)-1, query)

def first_occurance(keys, min_index, max_index, query):
    if keys[min_index] == query:
        return min_index
    if min_index == max_index:
        return -1
    mid_index = min_index + (max_index - min_index) // 2
    if keys[mid_index] >= query:
        return first_occurance(keys, min_index, mid_index, query)
    return first_occurance(keys, mid_index + 1, max_index, query)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
