# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        left, right = 0, n
        top, bottom = 0, m
        grid = [[-1] * n for _ in range(m)]

        directions = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        r, c, d = 0, 0, 0 # current row, col, direction 

        while head:
            dr, dc = directions[d]

            while (
                head and 
                left <= c < right and
                top <= r < bottom and
                grid[r][c] == -1
                
            ):
                grid[r][c] = head.val
                head = head.next
                r, c = r + dr, c + dc
            r, c = r - dr, c - dc #undoing the previous incr
            d = (d + 1) % 4
            dr, dc = directions[d]
            r, c = r + dr, c + dc
            
        return grid