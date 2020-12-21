from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  
  Q = deque()
  Q.append(root)
  while Q:
    level_nd_list = []
    level_val_list = []
    while Q:
      nd = Q.popleft()
      level_val_list.append(nd.val)
      if nd.left:
        level_nd_list.append(nd.left)
      if nd.right:
        level_nd_list.append(nd.right)

    # compute average of the level
    result.append(sum(level_val_list)/len(level_val_list))

    for nd in level_nd_list:
      Q.append(nd)

  return result



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level averages are: " + str(find_level_averages(root)))
