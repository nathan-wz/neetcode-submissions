class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""

        for i in range(len(strs[0])):
            focusLetter = strs[0][i]
            
            for j in range(len(strs)):
                if i >= len(strs[j]): 
                    return commonPrefix

                currentLetter = strs[j][i]

                if currentLetter != focusLetter:
                    return commonPrefix
            
            commonPrefix += focusLetter
        
        return commonPrefix