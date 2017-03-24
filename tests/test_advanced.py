# -*- coding: utf-8 -*-

from .context import lirix

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(lirix.hmm())


if __name__ == '__main__':
    unittest.main()
