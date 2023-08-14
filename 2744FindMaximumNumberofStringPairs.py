class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] == (words[j])[::-1]:
                    count += 1
                    continue
        return count

a = Solution()
print(a.maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"]))
Output: 2
            
