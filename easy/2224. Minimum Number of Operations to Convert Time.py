class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        minut1 =(int(current[:2]) ) * 60 + int(current[3:])
        minut2 =(int(correct[:2]) ) * 60 + int(correct[3:])
        farq = minut2 - minut1
        count =0
        count += farq // 60
        farq = farq - 60 * (farq // 60) 
        count += farq // 15
        farq = farq - 15 * (farq // 15)
        count += farq // 5
        farq = farq - 5 * (farq // 5)
        count += farq
        return count
        #problem solved
        # return farq // 60 + (farq % 60) // 15 + (((farq % 60) // 15 ) % 15) // 5 + ((((farq % 60) // 15 ) % 15) // 5) % 5
a = Solution()
print(a.convertTime( current = "00:00", correct = "23:59")) 
Output: 3