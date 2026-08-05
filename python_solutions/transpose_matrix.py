from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix[0])
        columns=len(matrix)

        transposed = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                transposed[i][j]=matrix[j][i]
       
        return transposed
    
if __name__ == "__main__":
    solution = Solution()
    initial = [
        [1, 2, 3], 
        [4, 5, 6]
    ]
    print(solution.transpose(initial))