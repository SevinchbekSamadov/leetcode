class Solution:
    def sumOfMultiples(self, n: int) -> int:
        #3 or 5 or 7
        def getResult():
            for i in range(1, n + 1):
                if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                    yield i
        return sum(getResult())

        # summ = 0
        # for i in range(1,n+1):
        #     if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        #         summ += i
        # return summ



a = Solution()
print(a.sumOfMultiples(n = 10))
#40