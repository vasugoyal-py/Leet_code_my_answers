class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        leng = (m*n) - 1

        r = leng
        l = 0

        if n == 1:
            while l <= r:
                mid = (l+r) // 2

                if matrix[0][mid] == target:
                    return True
                elif matrix[0][mid] > target:
                    r = mid - 1
                elif matrix[0][mid] < target:
                    l = mid + 1
        else:
            while l <= r:
                mid = (l + r) // 2
                i = mid // m
                j = mid % m

                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    r = mid - 1
                elif matrix[i][j] < target:
                    l = mid + 1
        return False

