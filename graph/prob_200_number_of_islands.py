class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n)
        return count
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i == m or j == n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)


https://interview.google.com/virtual/edc9196f-f0f6-4c9e-afb5-7b50f78de9d0