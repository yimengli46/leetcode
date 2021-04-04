from collections import deque

def can_construct(originalSeq, sequences):
	# a. Initialize the graph
	tasks = []
	for seq in sequences:
		for s in seq:
			if s not in tasks:
				tasks.append(s)

	if len(tasks) != len(originalSeq):
		return False

	inDegree = {i: 0 for i in tasks} # count of incoming edges
	graph = {i: [] for i in tasks}	 # adjacency list graph

	# b. Build the graph
	for seq in sequences:
		len_seq = len(seq)
		for i in range(0, len_seq-1):
			parent, child = seq[i], seq[i+1]
			if child not in graph[parent]:
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
	idx = 0
	while sources:
		if len(sources) > 1: # more than one source node to choose from
			return False
		if sources[0] != originalSeq[idx]:
			return False

		vertex = sources.popleft()
		sortedOrder.append(vertex)
		idx += 1

		for child in graph[vertex]: # get the node's children to decrement their in-degrees
			inDegree[child] -= 1
			if inDegree[child] == 0:
				sources.append(child)

	
	return len(sortedOrder) == len(tasks)




print("Can construct: " +
			str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
#assert 1==2
print("Can construct: " +
			str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
print("Can construct: " +
			str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))

