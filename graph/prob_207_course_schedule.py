class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        ## build the graph
        self.graph_ = {}

        for p in prerequisites:
            first, second = p
            if second in self.graph_:
                self.graph_[second].append(first)
            else:
                self.graph_[second] = [first]

        ## states: white = unknown, gray = visiting, black = visited
        self.visiting = {}
        for course in range(numCourses):
            self.visiting[course] = 'white'

        for i in range(numCourses):
            if self.dfs(i):
                return False

        return True


    def dfs(self, course):
        print('visiting node {} ...'.format(course))
        if self.visiting[course] == 'gray':
            print('node {} is gray. Cycle detected. return.'.format(course))
            return True # there is a cycle
        if self.visiting[course] == 'black':
            print('node {} is black. No cycle. return'.format(course))
            return False

        self.visiting[course] = 'gray'

        if course in self.graph_.keys():
            neis = self.graph_[course]
            for nei in neis:
                if self.dfs(nei):
                    return True

        self.visiting[course] = 'black'
        print('finish visiting node {}'.format(course))

        return False

#========================================================================================
numCourses = 2
prerequisites = [[1,0]]

sol = Solution()
ans = sol.canFinish(numCourses, prerequisites)
print('ans = {}'.format(ans))
print('---------------------------------------------------------------------')
numCourses = 2
prerequisites = [[1,0],[0,1]]
ans = sol.canFinish(numCourses, prerequisites)
print('ans = {}'.format(ans))
print('---------------------------------------------------------------------')
numCourses = 8
prerequisites = [[1,0], [2,6], [1,7], [6,4], [7,0], [0,5]]
ans = sol.canFinish(numCourses, prerequisites)
print('ans = {}'.format(ans))