class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        up = [i for i in range(m)]

        down = [m - 1 - i for i in range(m)]

        for _ in range(3, n + 1):

            new_up = [0] * m

            new_down = [0] * m

            total = 0

            for i in range(m):

                new_up[i] = total

                total = (total + down[i]) % MOD

            total = 0

            for i in range(m - 1, -1, -1):

                new_down[i] = total

                total = (total + up[i]) % MOD

            up = new_up

            down = new_down

        return (sum(up) + sum(down)) % MOD