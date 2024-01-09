import pytest
from math import floor


class Solution:
    def solve(self, x: int) -> int:
        eps = 10e-3
        x0 = 0
        x1 = x / 2
        while abs(x1 - x0) > eps:
            x0 = x1
            x1 = 0.5 * (x0 + x / x0)
        return floor(x1)


@pytest.mark.parametrize("x, expected_value", [
    (2, 1), (3, 1), (8, 2), (16, 4), (26, 5)
])
def test_problem(x, expected_value):
    solution = Solution()
    ans = solution.solve(x)
    assert ans == expected_value
