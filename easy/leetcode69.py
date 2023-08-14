class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        for i in range(x):
            for j in range(x//2 + 1):
                 a = j
                 if a * a == x:
                      break
            x -= 1
        return a
                     


a = Solution()
print(a.mySqrt( x = 4))
#4
print(a.mySqrt( x = 2))
#2