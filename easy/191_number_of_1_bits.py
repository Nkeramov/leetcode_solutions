import pytest
from math import floor


class Solution:
    def solve(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 2
            n //= 2
        return ans


@pytest.mark.parametrize("x, expected_value", [
    (11, 3), (128, 1), (4294967293, 31)
])
def test_problem(x, expected_value):
    solution = Solution()
    ans = solution.solve(x)
    assert ans == expected_value
