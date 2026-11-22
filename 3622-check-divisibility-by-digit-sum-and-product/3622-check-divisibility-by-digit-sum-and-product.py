class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        return n % (sum(digits) + __import__('math').prod(digits)) == 0