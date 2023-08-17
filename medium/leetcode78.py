class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        pass
        # subset = [[]]
        # for i in range(len(nums)):
        #     subset1 = []
        #     for j in range(i,len(nums)):
        #         for l in range(nums)
        #         subset1.append(nums[j])
        #     subset.append(subset1)
        # for i in range(1,pow(2,len(nums))):
        #     subset.append(nums[i % len(nums)])
        # return subset
a = Solution()
print(a.subsets(nums = [1,2,3]))
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        pass 

a = Solution()
print(a.subsets(nums = [1,2,3]))
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
[1,2,3,4,5]
[][1][2][1,2][3][1,3][4][1,4][5][1,5][2,3][2,4]