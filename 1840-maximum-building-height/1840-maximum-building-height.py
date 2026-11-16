class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])

        restrictions.sort()


        for i in range(1, len(restrictions)):

            prev_id, prev_h = restrictions[i - 1]

            curr_id, curr_h = restrictions[i]

            restrictions[i][1] = min(

                curr_h, prev_h + curr_id - prev_id

            )


        for i in range(len(restrictions) - 2, -1, -1):

            curr_id, curr_h = restrictions[i]

            next_id, next_h = restrictions[i + 1]

            restrictions[i][1] = min(

                curr_h, next_h + next_id - curr_id

            )


        ans = 0

        for i in range(1, len(restrictions)):

            prev_id, prev_h = restrictions[i - 1]

            curr_id, curr_h = restrictions[i]

            distance = curr_id - prev_id

            peak = (prev_h + curr_h + distance) // 2

            ans = max(ans, peak)


        last_id, last_h = restrictions[-1]

        ans = max(ans, last_h + n - last_id)

        return ans