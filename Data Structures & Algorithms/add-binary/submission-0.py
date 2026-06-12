class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        # Check rightmost place
            # if 1 and 1, turn to 0 and add a carry
            # if 1 and 0 or 0 and 1, return 1
            # if 0 and 0, return 0, no carry
        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        carry = ["N"] * (maxLen + 1)
        a, b = a[::-1], b[::-1]
        for i in range(maxLen):
            if a[i] == "1" and b[i] == "1" and carry[i] == "N":
                res = res + "0"
                carry[i+1] = "Y"
            elif a[i] == "1" and b[i] == "1" and carry[i] == "Y":
                res = res + "1"
                carry[i+1] = "Y"
            elif ((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")) and carry[i] == "N":
                res = res + "1"
            elif ((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")) and carry[i] == "Y":
                res = res + "0"
                carry[i+1] = "Y"
            elif a[i] == "0" and b[i] == "0" and carry[i] == "N":
                res = res + "0"
            elif a[i] == "0" and b[i] == "0" and carry[i] == "Y":
                res = res + "1"
            
        
        if carry[-1] == "Y":
            res = res + "1"


        res = res[::-1]
        return res
        
