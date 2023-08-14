class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # j = 0
        # l = ''
        # k = len(strs[0])
        # s = strs[0]
        # for i in strs:
        #     if k > len(i):
        #         k = len(i)
        #         s = i
        # while j < len(s):
        #     m = 0
        #     for i in strs:
        #         if i.startswith(s[:j+1]):
        #             m += 1
        #     if m == len(strs):
        #         l += s[j]
        #     j += 1
        # return l
        #rasmiy yechim
        res = ' '
        strs = sorted(strs)
        return strs
        x = strs[0]
        y = strs[-1]
        for i in range(min(len(x),len(y))):
            if x[i] != y[i]:
                return res
            else:
                res += x[i]
        return res
    
    
            
    
        
                    
                 
prefix1 = Solution()
print(prefix1.longestCommonPrefix(["flower","flow","flight"]))
# Output: "fl"
print(prefix1.longestCommonPrefix(["dog","racecar","car"]))
# Output: ""
