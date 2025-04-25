import pytest


class Solution:
    def solve(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            ftrib = [0] * (n + 1)
            ftrib[:3] = [0, 1, 1]
            for i in range(3, n + 1):
                ftrib[i] = ftrib[i - 1] + ftrib[i - 2] + ftrib[i - 3]
            return ftrib[-1]


@pytest.mark.parametrize("n, expected_value", [
    (0, 0), (4, 4), (25, 1389537)
])
def test_problem(n, expected_value):
    solution = Solution()
    ans = solution.solve(n)
    assert ans == expected_value
