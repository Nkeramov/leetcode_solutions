import pytest


class Solution:
    def solve(self, s: str) -> str:
        if not s:
            return s
        left, right = 0, len(s)-1
        ans = list(s)
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                ans[left], ans[right] = ans[right], ans[left]
                left += 1
                right -= 1
            elif s[left].isalpha():
                right -= 1
            else:
                left += 1
        return ''.join(ans)


@pytest.mark.parametrize("input_value, expected_value", [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!")
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
