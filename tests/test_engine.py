import unittest
from src.modal.engine import Engine


class EngineTestCases(unittest.TestCase):
    """Tests for `engine.py`."""
    def test_engine_default_creation(self):
        """Is five successfully determined to be prime?"""
        engine = Engine()
        self.assertEqual(engine.get_name(), "engine")


if __name__ == '__main__':
    unittest.main()
