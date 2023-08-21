class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        answer = []
        row = king[0]
        column = king[1]
        for i in range(row + 1,8):
            a = [i,column] 
            if a in queens:
                answer.append(a)
                break
        for i in range(row - 1,-1,-1):
            a = [i,column] 
            if a in queens:
                answer.append(a)
                break
        for i in range(column + 1,8):   
            a = [row,i] 
            if a in queens:
                answer.append(a)
                break
        for i in range(column - 1,-1,-1):
            a = [row,i] 
            if a in queens:
                answer.append(a)
                break
        for i in range(8):
            a = [row + i, column + i]
            if a in queens:
                answer.append(a)
                break
        for i in range(8):
            a = [row - i, column - i]
            if a in queens:
                answer.append(a)
                break
        for i in range(8):
            a = [row + i, column - i]
            if a in queens:
                answer.append(a)
                break
        for i in range(8):
            a = [row - i, column + i]
            if a in queens:
                answer.append(a)
                break
        return answer


a = Solution()
print(a.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
Output: [[2,2],[3,4],[4,4]]
print(a.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],[0,0]))
[[0,1],[1,0],[3,3]]
