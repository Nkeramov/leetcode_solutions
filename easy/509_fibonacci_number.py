import pytest


class Solution:
    def solve(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            fib = [0] * (n + 1)
            fib[:3] = [0, 1, 1]
            for i in range(3, n + 1):
                fib[i] = fib[i - 1] + fib[i - 2]
            return fib[-1]


@pytest.mark.parametrize("n, expected_value", [
    (0, 0), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)
])
def test_problem(n, expected_value):
    solution = Solution()
    ans = solution.solve(n)
    assert ans == expected_value
