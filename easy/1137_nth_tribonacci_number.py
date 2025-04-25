import pytest


class Solution:
    def solve(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            ft = [0]*(n+1)
            ft[:3] = [0, 1, 1]
            for i in range(3, n+1):
                ft[i] = ft[i-1]+ft[i-2]+ft[i-3]
            return ft[-1]


@pytest.mark.parametrize("n, expected_value", [
    (4, 4),
    (25, 1389537)
])
def test_problem(n, expected_value):
    solution = Solution()
    ans = solution.solve(n)
    assert ans == expected_value
