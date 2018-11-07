# coding=utf-8
import unittest
from src.modal.engine import Engine


class EngineTestCases(unittest.TestCase):
    """Tests for `engine.py`."""
    def test_singleton(self):
        """Assert that not exception is raised"""
        with self.assertRaises(Exception) as context:
            # Trigger an exception if singleton is violated
            Engine()
            Engine()

        self.assertTrue("This class is a singleton! Call the instance methods"
                        in context.exception)

    def test_unicode(self):
        """Assert that no exception is made with texts with many unicode characters"""
        engine = Engine.get_instance()
        text = " I went to the super market and I was not hÀppÝ with yÝ experience¡. " \
               "امين افضل واحد" \
               "The line was super lârge and it wasted a lot of my time that I could have spent ∫¶ ∫¶ ∫¶ ∫¶" \
               " doing something else ÿŒ Œ Œ"
        #Check if the test with unicode is supported
        try:
            engine.get_text_sentiment_values(text)
            # Extreme case where the entire sentence is in UNICode characters
            text = "Åë Òé évˉ ïØ™ ïÒw Yb:@"
            engine.get_text_sentiment_values(text)
        except:
            self.fail("get_text_sentiment_values(text='%s') raised Exception unexpectedly!" % text)


if __name__ == '__main__':
    unittest.main()
