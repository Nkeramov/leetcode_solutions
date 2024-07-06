import pytest


class Solution:
    def solve(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        square = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
            return square
        return square - abs((max(ax1, bx1) - min(ax2, bx2)) * (max(ay1, by1) - min(ay2, by2)))


@pytest.mark.parametrize("ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected_value", [
    (-3, 0, 3, 4, 0, -1, 9, 2, 45),
    (-2, -2, 2, 2, -2, -2, 2, 2, 16)
])
def test_problem(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected_value):
    solution = Solution()
    ans = solution.solve(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    assert ans == expected_value
