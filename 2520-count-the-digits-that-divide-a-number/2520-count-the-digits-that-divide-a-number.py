class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        digit = 1
        orig = num
        while(num>0):
            digit = num%10
            num//=10
    
            if digit != 0:
                if orig%digit == 0:
                    count += 1
        return count
