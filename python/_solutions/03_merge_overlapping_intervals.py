import unittest


# Merge Overlapping Intervals
#
# You are given a list of intervals. Each interval is represented as
# [start, end], where start <= end.
#
# Merge every pair of intervals that overlaps, and return the resulting
# non-overlapping intervals ordered by their starting values.
#
# Two intervals overlap when they share at least one value. This means that
# [1, 4] and [4, 5] must be merged into [1, 5].
#
# The input intervals may be unsorted. An interval may also be completely
# contained inside another interval.
#
# Examples:
#   intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#   return [[1, 6], [8, 10], [15, 18]]
#
#   intervals = [[1, 4], [4, 5]]
#   return [[1, 5]]
#
# Constraints:
# - 0 <= len(intervals) <= 100000
# - Each interval contains exactly two integers.
# - intervals[i][0] <= intervals[i][1]
# - -1_000_000_000 <= intervals[i][j] <= 1_000_000_000
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()

    merged = [intervals[0].copy()]

    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current.copy())

    return merged

class MergeIntervalsTests(unittest.TestCase):
    def test_multiple_overlaps(self):
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_touching_boundaries_overlap(self):
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

    def test_unsorted_intervals(self):
        self.assertEqual(
            merge_intervals([[8, 10], [1, 3], [2, 6], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_contained_intervals(self):
        self.assertEqual(
            merge_intervals([[1, 10], [2, 3], [4, 8]]),
            [[1, 10]],
        )

    def test_negative_values(self):
        self.assertEqual(
            merge_intervals([[-8, -3], [-5, 0], [2, 4]]),
            [[-8, 0], [2, 4]],
        )

    def test_single_interval(self):
        self.assertEqual(merge_intervals([[3, 7]]), [[3, 7]])

    def test_empty_input(self):
        self.assertEqual(merge_intervals([]), [])

    def test_same_start_different_ends(self):
        self.assertEqual(
            merge_intervals([[1, 2], [1, 7], [1, 4]]),
            [[1, 7]],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
