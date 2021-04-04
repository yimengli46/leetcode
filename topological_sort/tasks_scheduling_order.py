from collections import deque

def find_order(tasks, prerequisites):
  sortedOrder = []

  if tasks <= 1:
  	return [0]

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)} # count of incoming edges
  graph = {i: [] for i in range(tasks)}   # adjacency list graph

  # b. Build the graph
  for edge in prerequisites:
    parent, child = edge[0], edge[1]
    graph[parent].append(child) # put the child into its parent's list
    inDegree[child] += 1 # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the source queue
  sortedOrder = []
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]: # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  if len(sortedOrder) < tasks:
  	return []

  return sortedOrder


print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
print("Is scheduling possible: " +
    str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
print("Is scheduling possible: " +
    str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
