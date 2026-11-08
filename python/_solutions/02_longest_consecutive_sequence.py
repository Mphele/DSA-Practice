import unittest


# Longest Consecutive Sequence
#
# Given an unsorted list of integers `nums`, return the length of the longest
# sequence of consecutive integer values.
#
# The values only need to exist in the list; they do not need to appear next to
# one another or be in the correct order in the original input.
# Duplicate values do not extend a sequence.
#
# Requirements:
# - Solve the problem in O(n) time.
#
# Examples:
#   nums = [100, 4, 200, 1, 3, 2]
#   return 4
#   Explanation: The longest sequence is [1, 2, 3, 4].
#
#   nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   return 9
#   Explanation: The longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].
#
# Constraints:
# - 0 <= len(nums) <= 100000
# - -1_000_000_000 <= nums[i] <= 1_000_000_000
def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set()
    for num in nums:
        num_set.add(num)

    max_con = 1


    for num in nums:
        current_num = num

        current_con = 1
        while current_num+1 in num_set:
            current_con +=1
            current_num+=1

        if current_con>max_con:
            max_con=current_con

    return max_con


class LongestConsecutiveTests(unittest.TestCase):
    def test_unsorted_values(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_long_sequence_with_duplicate(self):
        self.assertEqual(
            longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
            9,
        )

    def test_empty_list(self):
        self.assertEqual(longest_consecutive([]), 0)

    def test_duplicates_do_not_extend_sequence(self):
        self.assertEqual(longest_consecutive([1, 2, 0, 1]), 3)

    def test_negative_values(self):
        self.assertEqual(longest_consecutive([-1, -2, -3, 5]), 3)

    def test_single_value(self):
        self.assertEqual(longest_consecutive([7]), 1)

    def test_multiple_sequences(self):
        self.assertEqual(
            longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]),
            7,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
