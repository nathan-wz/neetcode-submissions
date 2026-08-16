class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        isLInRange = l < len(word1)
        isRInRange = r < len(word2)
        result = ""

        while isLInRange or isRInRange:
            isLInRange = l < len(word1)
            isRInRange = r < len(word2)

            if isLInRange:
                result += (word1[l])
            if isRInRange:
                result += (word2[r])
            
            l, r = l + 1, r + 1
        
        return result

        