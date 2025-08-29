# test_emotion_detection.py
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Unit test class for the emotion_detector function.
    """
    def test_emotion_detector_joy(self):
        """Test that the dominant emotion for a joyful statement is 'joy'."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """Test that the dominant emotion for an angry statement is 'anger'."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Test that the dominant emotion for a disgusting statement is 'disgust'."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        """Test that the dominant emotion for a sad statement is 'sadness'."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        """Test that the dominant emotion for a fearful statement is 'fear'."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()