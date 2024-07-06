import pytest
from typing import List


class Solution:
    def solve(self, digits: List[int]) -> List[int]:
        p = 1
        for i in range(len(digits) - 1, -1, -1):
            t = digits[i] + p
            digits[i] = t % 10
            p = t // 10
        if p > 0:
            digits.insert(0, p)
        return digits


@pytest.mark.parametrize("digits, expected_value", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1,0])
])
def test_problem(digits, expected_value):
    solution = Solution()
    ans = solution.solve(digits)
    assert ans == expected_value
