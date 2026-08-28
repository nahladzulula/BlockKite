# test_blockkite.py
"""
Tests for BlockKite module.
"""

import unittest
from blockkite import BlockKite

class TestBlockKite(unittest.TestCase):
    """Test cases for BlockKite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockKite()
        self.assertIsInstance(instance, BlockKite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockKite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
