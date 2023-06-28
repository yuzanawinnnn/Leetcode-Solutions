class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxiAltitude = 0
        cur_Altitude = 0
        for i in range(len(gain)):
            cur_Altitude = cur_Altitude + gain[i]
            maxiAltitude = max(maxiAltitude,cur_Altitude)
        return maxiAltitude
