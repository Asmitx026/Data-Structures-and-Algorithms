class Solution:
    def GCD(self, n1: int, n2: int):
        if n2 < n1:
            n1, n2 = n2, n1

        while n2!=0:
            n1, n2 = n2, n1%n2
        return n1

    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven = n*(n+1), n**2
        return self.GCD(sumOdd, sumEven)