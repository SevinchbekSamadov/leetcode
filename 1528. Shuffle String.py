class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        indice = sorted(indices)
        natija = ''
        def getResult():
            for i in indice:
                yield s[indices.index(i)]
        return ''.join(getResult()) # join() string larni birlashtiradi
        # for i in list(getResult()):
        #     natija += i
        # return natija
        # indice = sorted(indices)
        # natija = ''
        # for i in indice:
        #     natija += s[indices.index(i)]
        # return natija   


a =Solution()
print(a.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
# Output: "leetcode"