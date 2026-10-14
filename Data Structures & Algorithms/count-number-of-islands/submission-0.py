class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            directions = [
                [-1, 0],
                [0, -1],
                [1, 0],
                [0, 1]
            ]

            q = deque()
            q.append((i, j))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(0, rows) and c in range(0, cols) and (r, c) not in visited and grid[r][c] == "1":
                        visited.add((r, c))
                        q.append((r, c))

        island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    print((i, j))
                    island += 1
                    visited.add((i, j))
                    bfs(i, j)
        
        return island