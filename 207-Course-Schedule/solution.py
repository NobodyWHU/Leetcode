class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2 or len(prerequisites) < 2:
            return True
        while len(prerequisites) > 0:
            count = 0
            mask = [True for _ in range(numCourses)]
            for pre in prerequisites:
                mask[pre[0]] = False
            for pre in prerequisites:
                if mask[pre[1]]:
                    count += 1
                    prerequisites.remove(pre)
            if len(prerequisites) == 0:
                return True
            elif count == 0:
                return False
        return False
            