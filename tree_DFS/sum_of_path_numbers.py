class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_path_numbers(root):
  return find_paths_recursive(root, 0)

def find_paths_recursive(currentNode, pathSum):
  if currentNode is None:
    return 0

  # add the current node to the path
  pathSum = 10*pathSum + currentNode.val

  if currentNode.left is None and currentNode.right is None:
    return pathSum
  
  return find_paths_recursive(currentNode.left, pathSum) + find_paths_recursive(currentNode.right, pathSum)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
