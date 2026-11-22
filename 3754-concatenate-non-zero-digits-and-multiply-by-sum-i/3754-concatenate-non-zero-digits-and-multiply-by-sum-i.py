class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ''.join(c for c in str(n) if c != '0')
        x = int(s) if s else 0
        return x * sum(int(c) for c in s)