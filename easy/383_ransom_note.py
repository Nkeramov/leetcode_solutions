import pytest

class Solution:
    def solve(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for c in ransomNote:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c, cnt in d.items():
            if magazine.count(c) < cnt:
                return False
        return True


@pytest.mark.parametrize("ransom_note, magazine, expected_value", [
    ("a", "b", False),
    ("aa", "b", False),
    ("aa", "ab", False),
    ("aa", "ab", False)
])
def test_problem(ransom_note, magazine, expected_value):
    solution = Solution()
    assert solution.solve(ransom_note, magazine) == expected_value
