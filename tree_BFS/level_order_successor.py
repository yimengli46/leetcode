from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  flag_key_found = False

  Q = deque()
  Q.append(root)

  while Q:
    nd = Q.popleft()
    # return the node because previous node matches the key
    if flag_key_found:
      return nd

    # key is found
    if nd.val == key:
      flag_key_found = True

    if nd.left:
      Q.append(nd.left)
    if nd.right:
      Q.append(nd.right)

  return None



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
result = find_successor(root, 12)
if result:
  print(result.val)
result = find_successor(root, 9)
if result:
  print(result.val)
