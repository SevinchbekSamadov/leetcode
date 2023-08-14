class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []
        for i in words:
            for j in words:
                if i in j:
                    if i != j:
                        res.append(i)
        return list(set(res))                    

a = Solution()
print(a.stringMatching(words = ["mass","as","hero","superhero"]))
Output: ["as","hero"]   