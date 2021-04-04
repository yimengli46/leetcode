from collections import deque

def find_trees(nodes, edges):
	# a. Initialize the graph
	inDegree = {i: 0 for i in range(nodes)} # count of incoming edges
	graph = {i: [] for i in range(nodes)}	 # adjacency list graph

	# b. Build the graph
	for edge in edges:
		parent, child = edge[0], edge[1]
		graph[parent].append(child) # put the child into its parent's list
		inDegree[child] += 1 # increment child's inDegree
		parent, child = edge[1], edge[0]
		graph[parent].append(child) # put the child into its parent's list
		inDegree[child] += 1 # increment child's inDegree

	#print('inDegree = {}'.format(inDegree))
	#print('graph = {}'.format(graph))

	# c. Find all sources i.e., all vertices with 0 in-degrees
	sources = deque()
	max_inDegree = -1
	for key in inDegree:
		if inDegree[key] == 1:
			sources.append(key)
		if inDegree[key] >= max_inDegree:
			max_inDegree = inDegree[key]
	#print('sources = {}'.format(sources))
	#assert 1==2
	if max_inDegree == 1 or max_inDegree == 0:
		return sources

	# d. for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
	# if a child's in-degree becomes zero, add it to the source queue
	while True:

		sources_list = []
		while sources:
			vertex = sources.popleft()
			for child in graph[vertex]:
				if inDegree[child] > 0:
					inDegree[child] -= 1
				if inDegree[vertex] > 0:
					inDegree[vertex] -= 1
				if inDegree[child] == 1:
					sources_list.append(child)
		#print('sources_list = {}'.format(sources_list))
		
		max_inDegree = -1
		for vertex in sources_list:
			if inDegree[vertex] >= max_inDegree:
				max_inDegree = inDegree[vertex]
				sources.append(vertex)

		#print('sources = {}'.format(sources))

		if max_inDegree == 1 or max_inDegree == 0:
			break

	return sources



print("Roots of MHTs: " +
		str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
#assert 1==2
print("Roots of MHTs: " +
		str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
print("Roots of MHTs: " +
		str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))
