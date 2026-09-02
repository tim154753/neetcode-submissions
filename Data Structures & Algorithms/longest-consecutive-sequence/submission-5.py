'''
Simple O(N^2) solution:
    - For each element nums[i], iterate through list to find consecutive element. Repeat process from here.
    - Issue: might be like O(N!), idek. Tons of repeated operations. 

Idea: 
    - In one pass, keep track of any consecutive elements seen, maybe with a hashmap where key = element, value = consecutive element and/or its index.
    - Then, after this pass, iterate through hashmap. Find last element of value for each key and check if it exists with its own values elsewhere in the map. If so, combine. 
    - Example: [0,3,2,5,4,6,1,1]
        - {0:[1], 3:[4], 2:[], 5:[6], 4:[1], 6:[], 1:[]}
        - Then, iterate through and combine key-values like this:
            - 0:[1] -> check if 2 exists, if so pop its list -> 0:[1,2] -> check if 3 exists -> 0:[1,2,3,4] -> check if 5 exists -> 0:[1,2,3,4,5,6] -> check if 7 exists -> check remaining dict -> {0:[1,2,3,4,5,6],}
'''

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            res[num] = []
        for num in nums:
            if res.get(num-1) is not None:
                if len(res[num-1]) == 0:
                    res[num-1].append(num) 
                elif num != res[num-1][-1]:
                    res[num-1].append(num) 

        for key in list(res.keys()):
            if res.get(key) is not None:
                if res[key]:
                    possible_next = res[key][-1]
                    while res[possible_next]:
                        vals = res.pop(possible_next, [])
                        res[key].extend(vals)
                        possible_next = res[key][-1]
        if not list(res.values()):
            return 0
        else:
            return max(len(x) for x in list(res.values())) + 1