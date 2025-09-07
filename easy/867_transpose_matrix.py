import pytest
from typing import List


class Solution:
    def solve(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            ans.append(row)
        return ans



@pytest.mark.parametrize("matrix, expected_value", [
    ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
    ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]])
])
def test_problem(matrix, expected_value):
    solution = Solution()
    ans = solution.solve(matrix)
    assert ans == expected_value
