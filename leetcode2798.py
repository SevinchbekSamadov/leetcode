class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        s = 0 
        for i in range(len(hours)):
            if i >= target:
                s += 1
        return s
a = Solution()
print(a.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))