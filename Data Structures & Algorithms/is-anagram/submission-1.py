class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1
        
        for char in t:
            if char not in t_map:
                t_map[char] = 1
            else:
                t_map[char] += 1

        for key in s_map:
            if key not in t_map or s_map[key] != t_map[key]:
                return False

        return True