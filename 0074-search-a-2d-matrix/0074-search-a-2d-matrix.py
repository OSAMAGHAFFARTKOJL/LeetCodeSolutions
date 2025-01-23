class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])
        
        l = 0
        r = col - 1


        for i in range(rows):
            if matrix[i][l] <= target and target <= matrix[i][r]:
                while l <= r:
                    mid = (l+r) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
            
        return False