class Solution:
    def minPartitions(self, n: str) -> int:
        max1 = 0
        for i in n:
            if int(i) > max1:
                max1 =  int(i)
        return max1             

a = Solution()
print(a.minPartitions(n = "876"))
#8