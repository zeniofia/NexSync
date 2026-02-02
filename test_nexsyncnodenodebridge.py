# test_nexsyncnodenodebridge.py
"""
Tests for NexSyncNodeNodeBridge module.
"""

import unittest
from nexsyncnodenodebridge import NexSyncNodeNodeBridge

class TestNexSyncNodeNodeBridge(unittest.TestCase):
    """Test cases for NexSyncNodeNodeBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexSyncNodeNodeBridge()
        self.assertIsInstance(instance, NexSyncNodeNodeBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexSyncNodeNodeBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
