import pytest
from typing import List


class Solution:

    def solve(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if 0 <= left < len(nums) and nums[left] == target:
            a, b = left, left
            while a >= 0 and nums[a] == target:
                a -= 1
            while b < len(nums) and nums[b] == target:
                b += 1
            return [a + 1, b - 1]
        elif 0 <= right < len(nums) and nums[right] == target:
            a, b = right, right
            while a >= 0 and nums[a] == target:
                a -= 1
            while b < len(nums) and nums[b] == target:
                b += 1
            return [a + 1, b - 1]
        else:
            return [-1, -1]

    def test(self):
        test_cases = [

        ]
        for i, test_case in enumerate(test_cases):
            ans = self.solve(test_case[0], test_case[1])
            correct_ans = test_case[-1]
            assert ans == correct_ans, f"Case {i} error, your answer is {ans}, but correct answer is {correct_ans}"
        print("All tests are successfully")


@pytest.mark.parametrize("nums, target, expected_value", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([1, 2, 2], 2, [1, 2])
])
def test_problem(nums, target, expected_value):
    solution = Solution()
    ans = solution.solve(nums, target)
    assert ans == expected_value
