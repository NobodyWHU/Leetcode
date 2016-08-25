# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.content = []
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        while p:
            self.content.append(p.val)
            p = p.next
        import random
        return self.content[random.randint(0,len(self.content)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()