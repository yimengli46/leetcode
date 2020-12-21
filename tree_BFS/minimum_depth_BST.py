class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

from collections import deque

def find_minimum_depth(root):
  count_level = 0

  Q = deque()
  Q.append(root)
  while Q:
    level_nd_list = []

    count_level += 1

    while Q:
      nd = Q.popleft()

      if not nd.left and not nd.right:
        return count_level

      if nd.left:
        level_nd_list.append(nd.left)
      if nd.right:
        level_nd_list.append(nd.right)

    for nd in level_nd_list:
      Q.append(nd)

  return count_level

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
