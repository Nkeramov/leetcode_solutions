import pytest
from typing import List



class Solution:
    def solve(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]


@pytest.mark.parametrize("first_input_array, second_input_array, expected_value", [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([1, 2, 7, 9], [3, 5, 11], 5.0)
])
def test_problem(first_input_array, second_input_array, expected_value):
    solution = Solution()
    assert solution.solve(first_input_array, second_input_array) == expected_value
