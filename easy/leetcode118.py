class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        answer = [[1]]
        a = [1]
        for j in range(numRows - 1):
            temp = [1]
            for i in range(len(a) - 1):
                temp.append(a[i] + a[i + 1] )
            temp.append(1)
            answer.append(temp)
            a = temp
        return answer

            
a = Solution()
print(a.generate(numRows = 10))
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]