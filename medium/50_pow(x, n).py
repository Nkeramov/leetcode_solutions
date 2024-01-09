import pytest


class Solution:
    def solve(self, x: float, n: int) -> float:
        return self.pow(x, n) if n >= 0 else 1.0 / self.pow(x, -n)

    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n % 2 == 0:
            return self.pow(x * x, n // 2)
        else:
            return x * self.pow(x * x, (n - 1) // 2)


@pytest.mark.parametrize("x, n, expected_value", [
    (2.00000, 10, 1024.00000), (2.10000, 3, 9.26100), (2.00000, -2, 0.25000)
])
def test_problem(x, n, expected_value):
    solution = Solution()
    ans = solution.solve(x, n)
    assert round(ans, 5) == expected_value
