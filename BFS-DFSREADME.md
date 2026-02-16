# BFS & DFS Problems

   Graph traversal algorithms - Week 1-2 focus.

   ## Problems Solved:
1. Number of Islands (Medium) - Connected components
2. Max Area of Island (Medium) - BFS with counting
3. Flood Fill (Easy) - Classic BFS
4. Rotting Oranges (Medium) - Multi-source BFS, time tracking
5. 01 Matrix (Medium) - Multi-source BFS, distance to 0s
6. Shortest Path in Binary Matrix (Medium) - 8-directional BFS
7. As Far from Land as Possible (Medium) - Multi-source BFS, distance to 1s

Day 4 Breakthrough: Solved As Far from Land as Possible in 16 minutes! 
Pattern recognition is clicking

   ## Patterns Learned:
- Single-source BFS** - Start from one cell
- Multi-source BFS** - Start from multiple cells simultaneously
- Grid traversal** - 4-directional movement
- Connected components** - Finding groups
- Distance calculation** - Shortest path in unweighted grid
- Level-order processing** - Processing by distance/time

Techniques:
- Using `deque` for efficient queue operations
- Visited tracking with sets or markers (-1, infinity)
- Direction arrays: `[(0,1), (0,-1), (1,0), (-1,0)]`
- Time tracking in queue: `(row, col, time)`
- Distance tracking: `result[nr][nc] = result[row][col] + 1`
