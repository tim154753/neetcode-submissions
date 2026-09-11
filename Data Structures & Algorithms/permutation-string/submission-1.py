'''
How tf do we do this without a hashmap or brute force "is in" checks, since we only have O(1) space and O(n) time?
    - Counters are O(1) space because there are at most 26 letters. LOL
    - Issue: cannot make counter for each susbtring within s2 because this would be O(len(s1)), leading to a total of O(len(s2) * len(s1)). 
    - Instead, we can keep a running total of counts just like in the last problem. Initialize counter. Then, when we move window to the right, decrement counts[s[l]] by 1, increment counts[s[r]] by 1. Then getting accurate counts is constant time. Yay
        - Checking dict equality is actually O(n), where n is the number of keys. So, this equality check is adding a factor of len(s1) to time complexity.
            - Can optimize further. Instead of a full counter for the window, we can probably just check if s2[r] is in s1's counter. If it's not, then we skip l and r to r+1 and iterate until we either find an element of s2 that isn't in s1 (then immediately skip l and r to r+1) or we exceed s1's length. In that case, we check 
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        l = 0
        r = len(s1) - 1
        window_count = Counter(s2[l:r+1])
        while r < len(s2) - 1:
            if window_count == s1_count:
                return True
            else:
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    window_count.pop(s2[l])
                l += 1
                r += 1
                window_count[s2[r]] = window_count.get(s2[r], 0) + 1
        if window_count == s1_count:
            return True
        return False
        