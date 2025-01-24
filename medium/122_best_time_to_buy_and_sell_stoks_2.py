import pytest
from typing import List


class Solution:
    def solve(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i-1])
        return ans


@pytest.mark.parametrize("input_value, expected_value", [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
