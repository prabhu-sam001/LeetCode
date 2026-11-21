class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []

        for c in first:
            left = first[c]
            right = last[c]
            i = left

            while i <= right:
                if first[s[i]] < left:
                    break
                right = max(right, last[s[i]])
                i += 1
            else:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev = -1

        for left, right in intervals:
            if left > prev:
                result.append(s[left:right + 1])
                prev = right

        return result