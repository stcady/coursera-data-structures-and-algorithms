# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def in_order_util(self, i):
    if i == -1:
      return
    self.in_order_util(self.left[i])
    self.result.append(self.key[i])
    self.in_order_util(self.right[i])

  def in_order(self):
    self.result = []
    self.in_order_util(0)
    return self.result

  def pre_order_util(self, i):
    if i == -1:
      return
    self.result.append(self.key[i])
    self.pre_order_util(self.left[i])
    self.pre_order_util(self.right[i])

  def pre_order(self):
    self.result = []
    self.pre_order_util(0)
    return self.result

  def post_order_util(self, i):
    if i == -1:
      return
    self.post_order_util(self.left[i])
    self.post_order_util(self.right[i])
    self.result.append(self.key[i])

  def post_order(self):
    self.result = []
    self.post_order_util(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.in_order()))
	print(" ".join(str(x) for x in tree.pre_order()))
	print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
