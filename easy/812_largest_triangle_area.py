import pytest
from typing import List


class Solution:
    def solve(self, points: List[List[int]]) -> float:
        ans = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]
                    ans = max(ans, abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        return ans


@pytest.mark.parametrize("points, expected_value", [
    ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.00000),
    ([[1, 0], [0, 0], [0, 1]], 0.50000)
])
def test_problem(points, expected_value):
    solution = Solution()
    ans = solution.solve(points)
    assert ans == expected_value
