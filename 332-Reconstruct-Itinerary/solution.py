class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        n = len(tickets)
        if n == 0:
            return []
        data = defaultdict(list)
        for f, t in tickets:
            data[f].append(t)
        for key in data.keys():
            data[key].sort(reverse=True)
        
        route = []
        def visit(airport):
            while data[airport]:
                visit(data[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]