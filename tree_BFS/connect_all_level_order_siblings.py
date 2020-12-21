from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next

def connect_all_siblings(root):
  Q = deque()
  Q.append(root)

  pre_nd = None
  while Q:
    level_nd_list = []
    
    while Q:
      nd = Q.popleft()

      if pre_nd:
        pre_nd.next = nd
      pre_nd = nd

      if nd.left:
        level_nd_list.append(nd.left)
      if nd.right:
        level_nd_list.append(nd.right)

    for nd in level_nd_list:
      Q.append(nd)



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_all_siblings(root)
root.print_tree()
