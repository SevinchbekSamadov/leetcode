class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # a = []
        # for i in range(n):
        #     a.append(nums[i])
        #     a.append(nums[n+i])
        # return a
        def get_result():
            for i in range(n):
                yield nums[i] , nums[i + n]
                # yield nums[i + n]
        a = get_result()
        return list(a)
a = Solution()
print(a.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(a.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
    
