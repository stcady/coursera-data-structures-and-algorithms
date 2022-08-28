from sys import stdin


def min_refills(distance, tank, stops):
    stop_count = 0
    i = 0
    limit = tank
    while limit < distance:
        if i >= len(stops) or stops[i] > limit:
            return -1
        while i < len(stops)-1 and stops[i+1] <= limit:
            i += 1
        stop_count += 1
        limit = tank + stops[i]
        i += 1
    return stop_count

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))