class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #we could have a search like this we initialize two pointers l = at beginning of the matrix
        #r at the end of the row in matrix, if the value of the target is larger than matrix[r] then we switch l = r and 
        #r will be the last value of the next row

        #once we find l < target < r we do a binary search to find the value mid and return if it matches target if it doesnt then we return false

        if not matrix or not matrix[0]:
            return False
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if matrix[row][0] <= target <= matrix[row][COLS - 1]:
                l , r = 0, COLS - 1

                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][mid] == target:
                        return True
                    if matrix[row][mid] < target:
                        l = mid + 1
                    else:
                        r =  mid - 1
                return False
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                top = row + 1
        return False                



