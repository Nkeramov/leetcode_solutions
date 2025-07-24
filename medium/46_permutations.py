import pytest
from typing import List

class Solution:
    def solve(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        return self.backtrack(nums, [], visited)


    def backtrack(self, nums, path, visited):
        ans = []
        if len(path) == len(nums):
            return [path]
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                ans.extend(self.backtrack(nums, path + [nums[i]], visited))
                visited[i] = False
        return ans


@pytest.mark.parametrize("nums, expected_value", [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]])
])
def test_problem(nums, expected_value):
    solution = Solution()
    ans = solution.solve(nums)
    assert ans == expected_value
