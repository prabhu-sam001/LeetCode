class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count = [0] * 100001

        for cost in costs:

            count[cost] += 1

        ans = 0

        for i in range(1, 100001):

            if coins < i:

                break

            buy = min(count[i], coins // i)

            ans += buy

            coins -= buy * i

        return ans       