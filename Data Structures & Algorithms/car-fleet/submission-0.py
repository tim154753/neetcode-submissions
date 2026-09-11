class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {pos:spd for pos, spd in zip(position, speed)}
        position.sort()
        time = float('-inf')
        l = len(position) - 1
        fleets = 0
        while l >= 0:
            car = position[l]
            arrive = float(target-car)/float(mp[car])
            if arrive > time:
                fleets += 1
                time = arrive
            l -= 1
        return fleets