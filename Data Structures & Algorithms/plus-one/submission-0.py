class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        carry = 1
        while carry != 0 and i >= 0:
            rem = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = rem
            i -= 1
        if carry == 1:
            return [1] + digits
        else:
            return digits
