import pytest


class Solution:
    def solve(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i + 1 < len(s):
                    if s[i + 1] == 'V':
                        ans += 4
                        i += 1
                    elif s[i + 1] == 'X':
                        ans += 9
                        i += 1
                    else:
                        ans += 1
                else:
                    ans += 1
            elif s[i] == 'X':
                if i + 1 < len(s):
                    if s[i + 1] == 'L':
                        ans += 40
                        i += 1
                    elif s[i + 1] == 'C':
                        ans += 90
                        i += 1
                    else:
                        ans += 10
                else:
                    ans += 10
            elif s[i] == 'C':
                if i + 1 < len(s):
                    if s[i + 1] == 'D':
                        ans += 400
                        i += 1
                    elif s[i + 1] == 'M':
                        ans += 900
                        i += 1
                    else:
                        ans += 100
                else:
                    ans += 100
            elif s[i] == 'V':
                ans += 5
            elif s[i] == 'L':
                ans += 50
            elif s[i] == 'D':
                ans += 500
            elif s[i] == 'M':
                ans += 1000
            i += 1
        return ans

    def solve2(self, s: str) -> int:
        ans = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in s:
            ans += d[i]
        if "IV" in s:
            ans -= 2
        if "IX" in s:
            ans -= 2
        if "XL" in s:
            ans -= 20
        if "XC" in s:
            ans -= 20
        if "CD" in s:
            ans -= 200
        if "CM" in s:
            ans -= 200
        return ans


@pytest.mark.parametrize("input_value, expected_value", [
    ("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("IX", 9), ("", 0)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
