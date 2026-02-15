# BFS & DFS Problems

   Graph traversal algorithms - Week 1-2 focus.

   ## Problems Solved:
   1. Number of Islands (Medium)
   2. Max Area of Island (Medium)
   3. Flood Fill (Easy)
   4. Rotting Oranges (Medium)
   5. 01 Matrix (Medium) - Multi-source BFS, distance calculation

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
