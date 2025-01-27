import pytest
from typing import List


class Solution:
    def solve(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1


@pytest.mark.parametrize("input_list, target, expected_value", [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
    ([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 16, 4),
    ([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 2, 0),
    ([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 91, 9),
    ([], 5, -1)
])
def test_problem(input_list, target, expected_value):
    solution = Solution()
    ans = solution.solve(input_list, target)
    assert ans == expected_value
