class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]


        for i in range(n):

            for j in range(i + 1, n):

                length = j - i + 1

                for d in range(1, length):

                    if length % d != 0:

                        continue

                    changes = 0

                    for r in range(d):

                        left = i + r

                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:

                            if s[left] != s[right]:

                                changes += 1

                            left += d

                            right -= d

                    cost[i][j] = min(cost[i][j], changes)


        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for t in range(1, k + 1):

            for i in range(2 * t, n + 1):

                for p in range(2 * (t - 1), i - 1):

                    dp[t][i] = min(

                        dp[t][i],

                        dp[t - 1][p] + cost[p][i - 1]

                    )

        return dp[k][n]