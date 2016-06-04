class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)
        

    # @return an integer
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    # @return an boolean
    def empty(self):
        return self.queue == []
        