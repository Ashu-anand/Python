class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len (s) != len (t): return False
        for idx, val in enumerate (s):
            if (val in hashmap_s and hashmap_s[val] != t[idx]) or (t[idx] in hashmap_t and hashmap_t[t[idx]] != val):
                return False
            else:
                hashmap_s[val] = t[idx]
                hashmap_t[t[idx]] = val
        return True


s = Solution ()
SS = "badc"
t = "baba"
print (s.isIsomorphic (SS, t))
