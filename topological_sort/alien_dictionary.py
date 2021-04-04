from collections import deque

def find_order(words):
	# extract the characters
	characters = []
	for word in words:
		for c in word:
			if c not in characters:
				characters.append(c)

	# a. Initialize the graph
	num_chs = len(characters)
	inDegree = {characters[i]: 0 for i in range(num_chs)} # count of incoming edges
	graph = {characters[i]: [] for i in range(num_chs)}	 # adjacency list graph

	num_words = len(words)
	# compare each pair of words
	for i in range(0, num_words-1):
		word_0 = words[i]
		word_1 = words[i+1]
		#print('w0 = {}, w1 = {}'.format(word_0, word_1))

		len_word_0 = len(word_0)
		flag_decoded = False
		for j in range(len_word_0):
			if flag_decoded:
				break
			c0 = word_0[j]
			c1 = word_1[j]
			if c0 != c1: # build a rule
				flag_decoded = True
				if c1 not in graph[c0]:
					graph[c0].append(c1)
					inDegree[c1] += 1
					

		#print('inDegree = {}'.format(inDegree))
		#print('graph = {}'.format(graph))

	# c. Find all sources i.e., all vertices with 0 in-degrees
	sources = deque()
	for key in inDegree:
		if inDegree[key] == 0:
			sources.append(key)

	# d. for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
	# if a child's in-degree becomes zero, add it to the source queue
	sortedOrder = ''
	while sources:
		vertex = sources.popleft()
		sortedOrder += vertex
		for child in graph[vertex]: # get the node's children to decrement their in-degrees
			inDegree[child] -= 1
			if inDegree[child] == 0:
				sources.append(child)

	if len(sortedOrder) < num_chs:
		return ""

	return sortedOrder



print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
#assert 1==2
print("Character order: " + find_order(["cab", "aaa", "aab"]))
print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
