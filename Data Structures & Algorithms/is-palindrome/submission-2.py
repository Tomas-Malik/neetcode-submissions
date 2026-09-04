class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        a = 0
        b = len(s)-1
        l = len(s) // 2
        flag = False
        for i in range(l):
            while not s[a].isalnum() and a < b:
                a += 1
            
            while not s[b].isalnum() and b > a:
                b -= 1

            if a>=b:
                return True
            
            
            
            
            if s[a] != s[b]:
                return False
            a +=1
            b -=1
        return True