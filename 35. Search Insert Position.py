class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        min1 = target
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] <= target and min1 >= target - nums[i]:
                    min1 = target - nums[i] 
                    # print(min1)
            return nums.index(nums[i]) + min1 

             

a =Solution()
print(a.searchInsert(nums = [1,3,5,6], target = 5))
#2
print(a.searchInsert(nums = [1,3,5,6], target = 2))
#1
print(a.searchInsert(nums = [1,3,5,6], target = 2))
#4