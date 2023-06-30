class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        import re
        license_key = ""
        s = list(re.sub(r'-', '', s).upper())
        s = s[::-1]
        for i in range(len(s)):
            if((i+1)%k == 0 and i!=len(s)-1):
                license_key = license_key + s[i] + "-"
            else:
                license_key = license_key + s[i]
        return license_key[::-1]

            
