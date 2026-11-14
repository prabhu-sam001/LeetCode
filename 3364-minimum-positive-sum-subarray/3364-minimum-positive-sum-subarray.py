class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)


        prefix = [0] * (n + 1)

        for i in range(n):

            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        for length in range(l, r + 1):

            for i in range(n - length + 1):

                curr_sum = prefix[i + length] - prefix[i]

                if curr_sum > 0:

                    ans = min(ans, curr_sum)

        return ans if ans != float('inf') else -1