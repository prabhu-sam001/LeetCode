class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        import bisect

        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        def update(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(bit, target):
            idx = 0
            mask = 1 << (m.bit_length() - 1)
            while mask:
                nxt = idx + mask
                if nxt <= m and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]
                mask >>= 1
            return idx + 1

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        costs = []
        total = 0

        for i in range(n):
            p = bisect.bisect_left(vals, nums[i]) + 1
            update(count, p, 1)
            update(sums, p, nums[i])
            total += nums[i]

            if i >= x:
                old = nums[i - x]
                p = bisect.bisect_left(vals, old) + 1
                update(count, p, -1)
                update(sums, p, -old)
                total -= old

            if i >= x - 1:
                mid_idx = kth(count, (x + 1) // 2)
                median = vals[mid_idx - 1]

                p = bisect.bisect_right(vals, median)
                left_count = query(count, p)
                left_sum = query(sums, p)

                cost = median * left_count - left_sum
                cost += total - left_sum - median * (x - left_count)

                costs.append(cost)

        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0] = [0] * (n + 1)

        for j in range(1, k + 1):
            for i in range(j * x, n + 1):
                dp[j][i] = min(
                    dp[j][i - 1],
                    dp[j - 1][i - x] + costs[i - x]
                )

        return dp[k][n]