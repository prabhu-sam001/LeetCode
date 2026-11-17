class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = [0] * 26

        for ch in text:

            count[ord(ch) - ord('a')] += 1

        b = count[1]

        a = count[0]

        l = count[11] // 2

        o = count[14] // 2

        n = count[13]

        return min(b, a, l, o, n)     