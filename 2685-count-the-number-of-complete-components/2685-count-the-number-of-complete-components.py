class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        ans = 0

        for i in range(n):
            if i not in visited:
                stack = [i]
                visited.add(i)
                nodes = 0
                degree_sum = 0

                while stack:
                    node = stack.pop()
                    nodes += 1
                    degree_sum += len(graph[node])

                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)

                if degree_sum == nodes * (nodes - 1):
                    ans += 1

        return ans