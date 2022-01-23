class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       
    #1. reverse the array
    #2. process the array by incrementing 1, and if digit is 9, then 0, and 1 carry. at the end add the carry to the array
    #3. again reverse the array and return it
    
        digits = digits[::-1]
        carry , i = 1, 0
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            
            else:
                digits.append(1)
                carry = 0
            i+=1
            
        return digits[::-1]