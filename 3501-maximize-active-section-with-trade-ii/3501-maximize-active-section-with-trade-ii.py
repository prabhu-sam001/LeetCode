import math
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        active = s.count('1')

        if '0' not in s:
            return [active] * len(queries)

        zeros = []
        idx = [0] * n

        for i in range(n):
            if s[i] == '0':
                if i and s[i - 1] == '0':
                    zeros[-1][1] += 1
                else:
                    zeros.append([i, 1])
            idx[i] = len(zeros) - 1

        m = len(zeros) - 1
        k = m.bit_length()

        st = [[0] * m for _ in range(max(k, 1))]

        for i in range(m):
            st[0][i] = zeros[i][1] + zeros[i + 1][1]

        for j in range(1, k):
            for i in range(m - (1 << j) + 1):
                st[j][i] = max(
                    st[j - 1][i],
                    st[j - 1][i + (1 << (j - 1))]
                )

        def query(l, r):
            if l > r or m <= 0:
                return 0
            j = (r - l + 1).bit_length() - 1
            return max(
                st[j][l],
                st[j][r - (1 << j) + 1]
            )

        ans = []

        for L, R in queries:
            iL, iR = idx[L], idx[R]

            cntL = -1 if iL < 0 else (
                zeros[iL][1] - (L - zeros[iL][0])
            )

            cntR = -1 if iR < 0 else (
                R - zeros[iR][0] + 1
            )

            start = iL + 1
            end = iR - (s[R] == '0')

            best = active

            if start < end:
                best = max(best, active + query(start, end - 1))

            if s[L] == '0' and s[R] == '0' and iL + 1 == iR:
                best = max(best, active + cntL + cntR)

            if s[L] == '0' and iL + 1 < iR + (s[R] == '1'):
                best = max(best, active + cntL + zeros[iL + 1][1])

            if s[R] == '0' and iL < iR - 1:
                best = max(best, active + cntR + zeros[iR - 1][1])

            ans.append(best)

        return ans