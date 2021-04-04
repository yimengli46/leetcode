from collections import deque

'''
def switch(parent, child):
	temp = parent
	parent = child
	child = temp
	return parent, child

def find_trees(num_nodes, edges):
	
	trees_height = []

	for node in range(num_nodes):

		inDegree = {i: 0 for i in range(num_nodes)} # count of incoming edges
		graph = {i: [] for i in range(num_nodes)}	 # adjacency list graph

		# b. Build the graph
		for edge in edges:	
			parent, child = edge[0], edge[1]
			if child <= node and parent <= node:
				parent, child = switch(parent, child)
			elif child >= node and parent >= node:
				parent, child = parent, child
			elif parent <= node and child >= node:
				parent, child = parent, child

			print('p = {}, c= {}'.format(parent, child))
			graph[parent].append(child) # put the child into its parent's list
			inDegree[child] += 1 # increment child's inDegree

		print('inDegree = {}'.format(inDegree))
		print('graph = {}'.format(graph))

		# c. Find all sources i.e., all vertices with 0 in-degrees
		sources = deque()
		for key in inDegree:
			if inDegree[key] == 0:
				sources.append(key)

		count_level = 1

		# d. for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
		# if a child's in-degree becomes zero, add it to the source queue
		while sources:
			vertex = sources.popleft()
			#sortedOrder.append(vertex)
			flag = False
			for child in graph[vertex]: # get the node's children to decrement their in-degrees
				inDegree[child] -= 1
				if inDegree[child] == 0:
					sources.append(child)
					flag = True
			if flag:
				count_level += 1
		print('count_level = {}'.format(count_level))
		trees_height.append(count_level)
	

	min_h = min(trees_height)
	min_nodes = []
	for node in range(num_nodes):
		if min_h == trees_height[node]:
			min_nodes.append(node)

	return min_nodes
'''

def find_trees(nodes, edges):
	if nodes <= 0:
		return []

	# with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
	if nodes == 1:
		return [0]

	# a. Initialize the graph
	inDegree = {i: 0 for i in range(nodes)}	# count of incoming edges
	graph = {i: [] for i in range(nodes)}	# adjacency list graph

	# b. Build the graph
	for edge in edges:
		n1, n2 = edge[0], edge[1]
		# since this is an undirected graph, therefore, add a link for both the nodes
		graph[n1].append(n2)
		graph[n2].append(n1)
		# increment the in-degrees of both the nodes
		inDegree[n1] += 1
		inDegree[n2] += 1

	# c. Find all leaves i.e., all nodes with 1 in-degrees
	leaves = deque()
	for key in inDegree:
		if inDegree[key] == 1:
			leaves.append(key)

	# d. Remove leaves level by level and subtract each leave's children's in-degrees.
	# Repeat this until we are left with 1 or 2 nodes, which will be our answer.
	# Any node that has already been a leaf cannot be the root of a minimum height tree, because
	# its adjacent non-leaf node will always be a better candidate.
	totalNodes = nodes
	while totalNodes > 2:
		leavesSize = len(leaves)
		totalNodes -= leavesSize
		for i in range(0, leavesSize):
			vertex = leaves.popleft()
			# get the node's children to decrement their in-degrees
			for child in graph[vertex]:
				inDegree[child] -= 1
				if inDegree[child] == 1:
					leaves.append(child)

	return list(leaves)



print("Roots of MHTs: " +
		str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
#assert 1==2
print("Roots of MHTs: " +
		str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
print("Roots of MHTs: " +
		str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))
