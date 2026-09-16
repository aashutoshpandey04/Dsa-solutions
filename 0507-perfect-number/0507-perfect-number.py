class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 5:
            return False
        Sum = 1
        for i in range(2,int(num**0.5) + 1):
            if num%i == 0:
                Sum += i
                if i * i != num:
                    Sum += num // i
        return Sum == num