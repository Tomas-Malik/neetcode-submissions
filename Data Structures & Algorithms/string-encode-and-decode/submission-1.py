class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            v = len(i)
            s = s + str(v) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        m = []
        p = list(s)

        while len(p) != 0:
            j = 0
            while p[j] != '#':
                j +=1
            num = int(''.join(p[0:j]))
            m.append(''.join(p[j+1:num+j+1]))
            del p[:num+j+1]
            
        return m


