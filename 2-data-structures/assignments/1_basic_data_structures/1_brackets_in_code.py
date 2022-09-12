# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                last_opening_bracket, last_opening_position = opening_brackets_stack.pop()
                if not are_matching(last_opening_bracket, next):
                    return i + 1
    if len(opening_brackets_stack) != 0:
        last_opening_bracket, last_opening_position = opening_brackets_stack.pop()
        return last_opening_position + 1
    return None

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == None:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
