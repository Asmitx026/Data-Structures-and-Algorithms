class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        '''
        Simple Implementation, leads to O(n) time and space complexity
        '''

        min_distance, res = 101, -1
        for i, drone in enumerate(drones):
            distance = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
            if distance <= drone[2]:
                if min_distance > distance:
                    min_distance = distance
                    res = i
        
        return res