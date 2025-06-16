class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        e=[]
        if len(s)!=len(t):
            return False
        for i in  s:
            if i in t:
                s=s[1::]
                t=t.replace(i,'', 1)                
            else:
                return False
        return True
        