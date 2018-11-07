import unittest
from src.modal.engine import Engine


class EngineTestCases(unittest.TestCase):
    """Tests for `engine.py`."""
    def test_singleton(self):
        """Is five successfully determined to be prime?"""
        with self.assertRaises(Exception) as context:
            # Trigger an exception if singleton is violated
            Engine()
            Engine()

        self.assertTrue("This class is a singleton! Call the instance methods"
                        in context.exception)


if __name__ == '__main__':
    unittest.main()
