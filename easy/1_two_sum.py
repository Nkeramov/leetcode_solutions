import pytest
from typing import List


class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if d.get(num, i) != i:
                return [d[num], i]
            d[target - num] = i
        return []


@pytest.mark.parametrize("nums, target, expected_value", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
])
def test_problem(nums, target, expected_value):
    solution = Solution()
    ans = solution.solve(nums, target)
    assert ans == expected_value
