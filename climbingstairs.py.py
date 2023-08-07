class Solution:
    def climbStairs(self, n: int) -> int:
        s = 0
        for i in range(n//2 + 1):
            for j in range(n+1):
                k = 1
                k2 = 1
                if 2 * i + j ==n:
                    for t in range(i+1,j+i+1):
                        k *= t
                    for l in range(1,j+1):
                        k2 *= l
                    s += (k // k2 )
        return s
bb = Solution()
print(bb.climbStairs(3))
print(bb.climbStairs(1))
print(bb.climbStairs(2))

