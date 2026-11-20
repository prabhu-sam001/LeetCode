class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 1

        bit = [0] * (2 * n + 3)

        def update(i):

            while i < len(bit):

                bit[i] += 1

                i += i & -i

        def query(i):

            res = 0

            while i > 0:

                res += bit[i]

                i -= i & -i

            return res

        prefix = 0

        ans = 0

        update(offset)

        for num in nums:

            prefix += 1 if num == target else -1

            idx = prefix + offset

            ans += query(idx - 1)

            update(idx)

        return ans       