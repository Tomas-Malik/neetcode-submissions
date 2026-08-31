class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        s_len = len(s)
        if s_len != len(t):
            return False

        for i in range(s_len):
            
            if s[i] in map_s:
                map_s[s[i]] +=1
            else:
                map_s[s[i]] = 1
            if t[i] in map_t:
                map_t[t[i]] +=1
            else:
                map_t[t[i]] = 1
        
        for key, val in map_s.items():
            if key not in map_t:
                return False
            if map_t[key] != val:
                return False
        return True




