from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments_sorted = sorted(segments, key = lambda e: e[1])
    curr = segments_sorted[0].end
    points.append(curr)
    for s in segments_sorted:
        if s.start > curr:
            points.append(s.end)
            curr = s.end
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
