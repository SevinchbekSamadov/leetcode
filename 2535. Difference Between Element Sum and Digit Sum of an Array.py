class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        def getResult():
            for i in nums:
                while i > 0:
                    yield i % 10
                    i //= 10
        return sum(nums) - sum(list(getResult()))
        # summ = 0
        # for i in nums:
        #     # summ = 0
        #     while i > 0:
        #         summ +=i % 10
        #         i //= 10
        # return sum(nums) - summ
    
a = Solution()
print(a.differenceOfSum(nums = [1,15,6,3]))
#9
