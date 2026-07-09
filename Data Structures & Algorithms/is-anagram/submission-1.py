class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashMapS = {}
        hashMapT = {}
        
        for i in range(len(s)): #iterate thru s because both strings are the same length 
            hashMapS[s[i]] = 1 + hashMapS.get(s[i],0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i],0)

        for c in hashMapS:
            if hashMapS[c] != hashMapT.get(c, 0):
                return False
        
        return True


    #Time: O(s + t)
    #Space: O(s + t)
