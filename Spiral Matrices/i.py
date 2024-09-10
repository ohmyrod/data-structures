class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #populate all the i in top row
            for i in range(left,right):
                result.append(matrix[top][i])
            top += 1
            #populate all the i in rightmost col
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #populate all the i in bottom col
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom -= 1
            #populate all i in leftmost col
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left += 1
        return result

