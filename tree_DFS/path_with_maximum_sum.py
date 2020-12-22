import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_maximum_path_sum(root):
  a = Path()
  a.calculate_maximum_branch_sum(root)
  return a.maximum_path_sum

class Path:
  def __init__(self):
    self.maximum_path_sum = -math.inf

  def calculate_maximum_branch_sum(self, currentNode):
    if currentNode is None:
      return 0

    # compute left tree and right tree height
    leftTree_sum = self.calculate_maximum_branch_sum(currentNode.left)
    rightTree_sum = self.calculate_maximum_branch_sum(currentNode.right)

    # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
    leftTree_sum = max(leftTree_sum, 0)
    rightTree_sum = max(rightTree_sum, 0)

    # diameter is different from height
    subtree_sum = leftTree_sum + rightTree_sum + currentNode.val
    self.maximum_path_sum = max(self.maximum_path_sum, subtree_sum)

    # compute the height at this node
    branch_sum = max(leftTree_sum, rightTree_sum) + currentNode.val
    #print('currentNode.val = {}, branch_sum = {}'.format(currentNode.val, branch_sum))
    #print('maximum_path_sum = {}'.format(self.maximum_path_sum))
    return branch_sum

#'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
#assert 1==2


root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
#'''
root = TreeNode(-1)
root.left = TreeNode(-3)
print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

