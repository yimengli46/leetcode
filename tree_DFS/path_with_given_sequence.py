class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  return compare_path(root, 0, sequence)

def compare_path(node, progress_id, sequence):
  if node is None and progress_id == len(sequence):
    return True
  if node is None:
    return False

  #print('node.val = {}, sequence = {}'.format(node.val, sequence[progress_id]))

  if node.val == sequence[progress_id]:
    return compare_path(node.left, progress_id+1, sequence) or compare_path(node.right, progress_id+1, sequence)
  else:
    return False


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
