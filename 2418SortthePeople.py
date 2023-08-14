class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [names[heights.index(i)] for i in reversed(sorted(heights))]
    #problem has been solved 


a = Solution()
print(a.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
Output: ["Mary","Emma","John"]