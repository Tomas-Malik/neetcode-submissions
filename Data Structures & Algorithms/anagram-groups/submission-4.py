class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)  # tuple is hashable, works as dict key directly
            
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        
        return list(dct.values())