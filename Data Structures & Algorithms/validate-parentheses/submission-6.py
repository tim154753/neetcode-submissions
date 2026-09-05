from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        open = deque()
        mp = {'{':'}', '[':']', '(':')'}
        for ch in s:
            if ch in '([{':
                open.append(ch)
            elif len(open) > 0:
                if ch == mp[open[-1]]:
                    open.pop()
                else:
                    return False
            else:
                return False
        return not bool(open)
            