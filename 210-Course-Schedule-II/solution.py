class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degress = [0] * numCourses
        childs = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            degress[pair[0]] += 1
            childs[pair[1]].append(pair[0])
        
        courses = set(range(numCourses))
        flag = True
        ans = []
        while flag and len(courses):
            flag = False
            removelist = []
            for x in courses:
                if degress[x] == 0:
                    for child in childs[x]:
                        degress[child] -= 1
                    removelist.append(x)
                    flag = True
            for x in removelist:
                ans.append(x)
                courses.remove(x)
        return ans if len(courses) == 0 else []