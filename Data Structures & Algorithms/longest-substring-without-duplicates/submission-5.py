class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        seen = {s[0]:0}
        l = 0
        r = 1
        best = 1
        while r < len(s):
            if seen.get(s[r]) is None or l > seen.get(s[r]):
                best = max(best, r-l+1)
                seen[s[r]] = r
                r += 1
            else:
                l = seen[s[r]] + 1
                seen[s[r]] = r
                r += 1
        return best