class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ins = []
        self.out = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.ins.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.out.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.out:
            while self.ins:
                self.out.append(self.ins.pop())
        return self.out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.ins)+len(self.out)) == 0