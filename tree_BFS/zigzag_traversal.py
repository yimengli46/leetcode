from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  
  Q = deque()
  Q.append(root)
  leftToRight = True
  while Q:
    level_nd_list = []
    level_val_list = deque()
    while Q:
      nd = Q.popleft()

      if leftToRight:
        level_val_list.append(nd.val)
      else:
        level_val_list.appendleft(nd.val)

      if nd.left:
        level_nd_list.append(nd.left)
      if nd.right:
        level_nd_list.append(nd.right)
    
    result.append(list(level_val_list))

    for nd in level_nd_list:
      Q.append(nd)

    leftToRight = not leftToRight

  return result



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
print("Zigzag traversal: " + str(traverse(root)))