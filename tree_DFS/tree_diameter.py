class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0

  def find_diameter(self, root):
    self.calculate_height(root)
    return self.treeDiameter

  def calculate_height(self, currentNode):
    if currentNode is None:
      return 0

    # compute left tree and right tree height
    leftTreeHeight = self.calculate_height(currentNode.left)
    rightTreeHeight = self.calculate_height(currentNode.right)

    # diameter is different from height
    subtree_diameter = leftTreeHeight + rightTreeHeight + 1
    self.treeDiameter = max(self.treeDiameter, subtree_diameter)

    # compute the height at this node
    subtree_height = max(leftTreeHeight, rightTreeHeight) + 1
    return subtree_height


treeDiameter = TreeDiameter()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))