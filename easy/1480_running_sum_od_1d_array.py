import pytest
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i, x in enumerate(nums[1:], 1):
            ans[i] = ans[i - 1] + x
        return ans


@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
])
def test_problem(input_list, expected_list):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_list
