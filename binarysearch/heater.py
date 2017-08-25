
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # find the closest point in another array
        closet_point = 0
        heaters.sort()
        for house in houses:
            closet_point = max(closet_point, abs(house-self.bsfind(house, heaters)))
        return closet_point

    def bsfind(self, target, pool):
        l, r = 0, len(pool)-1
        res = 0
        while l<=r:
            m = l+(r-l)/2
            if target <= pool[m]:
                r = m-1
                res = m
            else:
                l = m+1
        return pool[res] if abs(pool[res-1]-target)> abs(pool[res]-target) else pool[res-1]