import pytest
from typing import List


class Solution:
    def solve(self, accounts: List[List[int]]) -> int:
        return max(sum(x) for x in accounts)


@pytest.mark.parametrize("input_list, expected_value", [
    ([[1, 2, 3], [3, 2, 1]], 6),
    ([[1, 5], [7, 3], [3, 5]], 10),
    ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17)
])
def test_problem(input_list, expected_value):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_value
