from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        ans = 0
        cost = 0
        r = n - 1

        for l in range(n - 1, -1, -1):
            x = nums[l]
            cnt = 1
            total = 0

            while q and q[0][0] <= x:
                v, c = q.popleft()
                cnt += c
                total += v * c

            cost += x * (cnt - 1) - total
            q.appendleft((x, cnt))

            while cost > k:
                v, c = q[-1]
                cost -= v - nums[r]
                if c == 1:
                    q.pop()
                else:
                    q[-1] = (v, c - 1)
                r -= 1

            ans += r - l + 1

        return ans