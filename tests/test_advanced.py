# -*- coding: utf-8 -*-

from .context import lirix

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    
    def test_load_lyrics(self):
        print(lirix.load_lyrics("Brel", "Quand on a que l' amour"))

    def test_write_epub(self):
        lirix.write_epub()



if __name__ == '__main__':
    unittest.main()
