import pytest
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        min1 = float('inf')
        min2 = float('inf')
        for x in nums:
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        ans = max(max1 * max2 * max3, max1 * min1 * min2)
        return ans


@pytest.mark.parametrize("nums, expected_value", [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4], 24),
    ([-1, -2, -3], -6),
    ([-5, 6, -7, 2, 4, -3], 210)
])
def test_problem(nums, expected_value):
    solution = Solution()
    ans = solution.solve(nums)
    assert ans == expected_value
