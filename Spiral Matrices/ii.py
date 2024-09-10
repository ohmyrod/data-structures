class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #create matrix of 0's
        matrix = [[0] * n for _ in range(n)]
        num = 1

        left, right = 0, n
        top, bottom = 0, n

        while left < right and top < bottom:
            #populate all the i in top row
            for i in range(left,right):
                matrix[top][i] = num
                num +=1 
            top += 1
            #populate all the i in rightmost col
            for i in range(top,bottom):
                matrix[i][right-1] = num
                num +=1
            right -= 1

            if not (left < right and top < bottom):
                break

            #populate all the i in bottom col
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i] = num
                num +=1
            bottom -= 1
            #populate all i in leftmost col
            for i in range(bottom-1,top-1,-1):
                matrix[i][left] = num
                num +=1
            left += 1
        return matrix
