class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        new_str = ""
        num = 0
        sign = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        for i in range(len(s)):
            if not new_str and not sign and s[i] == "-":
                sign = -1
                continue
            if not new_str and not sign and s[i] == "+":
                sign = 1
                continue
            
            if s[i] in ["+","-","."," "] or s[i].isalpha():
                break
            
            new_str += s[i]
            
        if not new_str:
            return 0
        
        for ch in new_str:
            # num * 10 + int(ch) must be ≤ INT_MAX, so to check if the next addition will overflow, we use this overflow check instead of num > INT_MAX or vice versa:
            if num > (INT_MAX - int(ch)) // 10:
                if sign == 1 or sign == 0:
                    return INT_MAX
                if sign == -1:
                    return INT_MIN
            # num += int(ch) * (10 ** i) -> inefficient so avoid building the number from left to right 
            num = num * 10 + int(ch)

        return num * sign if sign else num