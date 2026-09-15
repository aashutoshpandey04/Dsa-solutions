class Solution:
    def addDigits(self, num: int) -> int:
        sum = num
        while sum > 9:
            num = sum
            sum = 0
            while num > 0:
                digit = num % 10
                num //= 10
                sum += digit
        return sum
