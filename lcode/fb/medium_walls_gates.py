'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  
  '''
  
  Brute Force Solution: Time: O(M^2N^2) Space: O(MN)

Implement a BFS from each empty room to its nearest gate. We use a 2D array called distance to keep track 
of the distance from the starting point. It also implicitly tell us whether a position had been visited so it 
won't be inserted into the queue again.
distance[r1,c1] = distance[r, c] + 1
Optimzied Breadth First Solution: O(MN)

Instead of using each node to get to the nearest gate, think opposite.
Enqueue all possible gates into the queue and then do a BFS.
Mark the distance to a room with its parent + 1 i.e. length of path from gate to the room is length of path to 
reach its parent + 1.
Since BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1, the distance to an 
empty room must be the shortest.
Only add empty rooms to Q. This makes sure we have the distance to clostest gate for each room.
Time complexity : O(mn)
If you are having difficulty to derive the time complexity, start simple. Let us start with the case with only one gate. 
The breadth-first search takes at most m×n steps to reach all rooms, therefore the time complexity is O(mn). But what if you
are doing breadth-first search from k gates? Once we set a room's distance, we are basically marking it as visited, which 
means each room is visited at most once. Therefore, the time complexity does not depend on the number of gates and is O(mn).
Space complexity : O(mn). The space complexity depends on the queue's size. We insert at most m×n points into the queue.

  
  from collections import deque
class Solution(object):
    def add_all_gates(self, q, rooms):
        M, N = len(rooms), len(rooms[0])
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0: ##INSIGHT
                    q.append((i,j))
        return
    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        q = deque()
        self.add_all_gates(q, rooms)
        M, N, INF = len(rooms), len(rooms[0]), 2**31 - 1
        while len(q):
            x,y = q.popleft()
            for a,b in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0<=a<M and 0<=b<N and rooms[a][b] == INF:                
                    q.append((a,b))
                    rooms[a][b] = rooms[x][y] + 1
        return
