class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmosthigh = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmosthigh[i] = leftmax
        ans = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, leftmosthigh[i]) > height[i]:
                ans += min(rightmax, leftmosthigh[i]) - height[i]
        
        return ans