class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        alphabetRange = range(97, 123)
        numberRange = range(48, 58)

        while L <= R:
            leftAscii = ord(s[L].lower())
            rightAscii = ord(s[R].lower())

            if not (leftAscii in alphabetRange or leftAscii in numberRange):
                L += 1
                continue

            if not (rightAscii in alphabetRange or rightAscii in numberRange):
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True
        