import pytest
from typing import List


class Solution:
    def solve(self, strs: List[str]) -> str:
        ans = strs[0]
        n = len(strs)
        for i in range(1, n):
            while not strs[i].startswith(ans):
                ans = ans[:-1]
                if not ans:
                    return ""
        return ans


@pytest.mark.parametrize('input_value, expected_value', [(['flower', 'flow', 'flight'], 'fl'),
                                                         (['dog', 'racecar', 'car'], ''),
                                                         (['test', 'test', 'trace'], 't')])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
