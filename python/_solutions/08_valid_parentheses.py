import unittest


# Exercise 08: Valid Parentheses
#
# Source: https://leetcode.com/problems/valid-parentheses/
# Original difficulty: Easy
#
# Task:
# You are given a string containing only round, square, and curly brackets.
# Return True when every opening bracket is closed by the same bracket type,
# every closing bracket has a matching opener, and all pairs close in the
# correct order. Otherwise, return False.
#
# Examples:
#   brackets = "()[]{}"
#   return True
#
#   brackets = "([)]"
#   return False
#
# Constraints:
# - 1 <= len(brackets) <= 10_000
# - brackets contains only the characters ()[]{}
def has_valid_parentheses(brackets: str) -> bool:

    open_brackets = []

    for bracket in brackets:
        if bracket == "(" or bracket == "[" or bracket == "{":
            open_brackets.append(bracket)

        else:
            if len(open_brackets)>0:
                open = open_brackets.pop()
                pair = open+bracket
                if pair not in ["()", "[]", '{}']:
                    return False
            else:
                return False
    return True if len(open_brackets)==0 else False

print(has_valid_parentheses("()[]{}"))

class ValidParenthesesTests(unittest.TestCase):
    def test_single_pair(self):
        self.assertEqual(has_valid_parentheses("()"), True)

    def test_adjacent_pairs(self):
        self.assertEqual(has_valid_parentheses("()[]{}"), True)

    def test_nested_pairs(self):
        self.assertEqual(has_valid_parentheses("{[]}"), True)

    def test_mismatched_types(self):
        self.assertEqual(has_valid_parentheses("(]"), False)

    def test_wrong_closing_order(self):
        self.assertEqual(has_valid_parentheses("([)]"), False)

    def test_closer_without_opener(self):
        self.assertEqual(has_valid_parentheses("]"), False)

    def test_unclosed_openers(self):
        self.assertEqual(has_valid_parentheses("((("), False)

    def test_mixed_nested_and_adjacent_pairs(self):
        self.assertEqual(has_valid_parentheses("([]){}"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
