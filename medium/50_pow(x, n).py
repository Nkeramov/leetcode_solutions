import pytest


class Solution:
    def solve(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1.0 / x
            n = -n
        p = self.solve(x, n // 2)
        p = p * p
        if n % 2 == 0:
            return p
        else:
            return p * x


@pytest.mark.parametrize("x, n, expected_value", [
    (2.00000, 10, 1024.00000), (2.10000, 3, 9.26100), (2.00000, -2, 0.25000)
])
def test_problem(x, n, expected_value):
    solution = Solution()
    ans = solution.solve(x, n)
    assert round(ans, 5) == expected_value
