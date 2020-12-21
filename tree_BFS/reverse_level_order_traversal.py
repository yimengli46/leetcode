from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  Q = deque()
  Q.append(root)

  while Q:
    level_nodes = []
    level_vals  = []

    while Q:
      node = Q.popleft()
      level_vals.append(node.val)

      if node.left:
        level_nodes.append(node.left)
      if node.right:
        level_nodes.append(node.right)
        
    for nd in level_nodes:
      Q.append(nd)
    result.appendleft(level_vals)

  return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Reverse level order traversal: " + str(traverse(root)))