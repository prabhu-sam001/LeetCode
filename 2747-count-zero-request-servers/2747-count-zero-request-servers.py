class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [0] * len(queries)
        count = [0] * (n + 1)
        active = 0
        left = right = 0

        for t, idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= t:
                server, time = logs[right]
                if count[server] == 0:
                    active += 1
                count[server] += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server, time = logs[left]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans
        