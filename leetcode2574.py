class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        a = []
        for i in range(len(nums)):
            a.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return a

a = Solution()
print(a.leftRightDifference(nums = [10,4,8,3]))
Output: [15,1,11,22]