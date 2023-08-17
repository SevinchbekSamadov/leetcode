class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        test1 = []
        def get_res(n):
            test2 = []
            for i in range(len(n)):
                for j in range(i + 1, len(n)):
                    if n[i] == n[j]:
                        test2.append(1)
                    else:
                        test2.append(0)
            return test2
        for j in words:
            if get_res(j) == get_res(pattern):
                test1.append(j)
        return test1

a = Solution()
print(a.findAndReplacePattern(words = ["a","b","c"], pattern = "a"))
Output: ["a","b","c"]
print(a.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))