import pytest
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans^num
        return ans


@pytest.mark.parametrize("input_list, expected_value", [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1)
])
def test_problem(input_list, expected_value):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_value
