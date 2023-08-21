class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        max1 = 0
        sana = 0
        for i in range(n):
            for j in range(i + 1,n):
                count = 0
                for k in roads:
                    sana += 1
                    if (i in k) or (j in k):
                        count += 1
                if count > max1:
                    max1 = count
        print(sana)
        # return max1
        


a = Solution()
print(a.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))
#4
print(a.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
print(a.maximalNetworkRank( n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))