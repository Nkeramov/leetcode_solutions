import pytest
from typing import List
from bisect import bisect_left


class Solution:
    def solve(self, nums: List[int]) -> int:
        tmp = [nums[0]]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > tmp[-1]:
                tmp.append(nums[i])
                ans += 1
            else:
                ind = bisect_left(tmp, nums[i])
                tmp[ind] = nums[i]
        return ans


@pytest.mark.parametrize("nums, expected_value", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([0, 1, 0, 3, 2, 3], 4),
    ([0, 1, 0, 3, 2, 3, 3, 1, 2, 3, 4, 5], 6)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value


