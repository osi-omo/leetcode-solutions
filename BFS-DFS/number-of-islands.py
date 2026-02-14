"""
LeetCode #200 - Number of Islands
Difficulty: Medium
Topic: BFS, Graph

Problem: Count the number of islands in a 2D grid.

Approach: Use BFS to explore each island. When we find unvisited 
land, start BFS to mark all connected land as visited.

Date done: February 13, 2026

assistance - solo
"""

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        island_amt = 0
        map = grid

        def island_find_bulk(start_island_row,start_island_column):
            visited.add((start_island_row,start_island_column))
            que = deque([(start_island_row,start_island_column)])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while que:
                row, column = que.popleft()
                
                for dr,dc in directions:
                    nr,nc = row + dr,column + dc
                    if 0 <= nr < m and 0<= nc<n and (nr,nc) not in visited and map[nr][nc] == "1":
                        visited.add((nr,nc))
                        que.append((nr,nc))
        
        for row in range(m):
            for col in range(n):
                if map[row][col] == "1" and (row,col) not in visited:
                    island_amt +=1
                    island_find_bulk(row,col)
        
        return island_amt
