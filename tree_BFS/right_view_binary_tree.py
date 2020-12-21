from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  
  Q = deque()
  Q.append(root)

  result.append(root)
  
  while Q:
    level_nd_list = []
    while Q:
      nd = Q.popleft()

      if nd.left:
        level_nd_list.append(nd.left)
      if nd.right:
        level_nd_list.append(nd.right)
    
    # append the right most node of this level
    if len(level_nd_list) > 0:
      result.append(level_nd_list[-1])

    for nd in level_nd_list:
      Q.append(nd)

  return result



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)
result = tree_right_view(root)
print("Tree right view: ")
for node in result:
  print(str(node.val) + " ", end='')