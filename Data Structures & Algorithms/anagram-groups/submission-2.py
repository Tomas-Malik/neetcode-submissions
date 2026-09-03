class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        otp = []
        dct = {}
        for i in strs:
            if len(i) == 0:
                s = "ba1" #finish later adding to dictionary etc.
                if s in dct:
                    dct[s].append(i)
                else:
                    dct[s] = [i]
                continue
            v = sorted(i)
            s = ""
            ct = 1
            let = v[0]
            for j in range(len(v)-1):
                if let == v[j+1]:
                    ct += 1
                else:
                    s = s + let + str(ct)
                    let = v[j+1]
                    ct = 1
            s = s + let + str(ct)
            if s in dct:
                dct[s].append(i)
            else:
                dct[s] = [i]
        for key, val in dct.items():
            otp.append(val)
        return otp


                




            



        
        