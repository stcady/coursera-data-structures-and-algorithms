#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def is_binary_search_tree_util(i, minimum, maximum, tree):
  if i == -1:
    return True
  if tree[i][0] <= minimum or tree[i][0] >= maximum:
    return False
  return is_binary_search_tree_util(tree[i][1], minimum, tree[i][0], tree) and is_binary_search_tree_util(tree[i][2], tree[i][0]-1, maximum, tree)

def is_binary_search_tree(tree):
  if len(tree) == 0:
    return True
  return is_binary_search_tree_util(0, -math.inf, math.inf, tree)

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if is_binary_search_tree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
