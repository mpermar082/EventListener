# test_eventlistener.py
"""
Tests for EventListener module.
"""

import unittest
from eventlistener import EventListener

class TestEventListener(unittest.TestCase):
    """Test cases for EventListener class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EventListener()
        self.assertIsInstance(instance, EventListener)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EventListener()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
