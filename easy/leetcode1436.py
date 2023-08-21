class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        for i in range(len(paths)):
            count = 0
            for j in paths:
                if (paths[i])[1] in j:
                    count += 1
            if count == 1:
                return (paths[i])[1]




a = Solution()
print(a.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
"Sao Paulo"
