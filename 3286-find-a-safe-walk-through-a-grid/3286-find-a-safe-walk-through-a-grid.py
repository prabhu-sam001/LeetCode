class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        while heap:
            cost, r, c = heapq.heappop(heap)

            if cost > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return health - cost >= 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc))

        return False