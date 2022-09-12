# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.set = [None] * self.n

        def depth(self, i):
                if self.parent[i] == -1:
                        return 1
                if self.set[i]:
                        return self.set[i]
                self.set[i] = 1 + self.depth(self.parent[i])
                return self.set[i]

        def compute_height(self):
                return max([self.depth(index) for index in range(0, self.n)])


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
