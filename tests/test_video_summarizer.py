import unittest
import os
from src.video_summarizer import VideoSummarizer

class TestVideoSummarizer(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.api_key = os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            self.skipTest("MISTRAL_API_KEY not set in environment")
        self.summarizer = VideoSummarizer(api_key=self.api_key)

    def test_extract_audio(self):
        """Test audio extraction from video."""
        # This test requires a sample video file
        video_path = "tests/data/sample.mp4"
        if not os.path.exists(video_path):
            self.skipTest("Sample video file not found")
        
        output_path = "tests/data/test_audio.wav"
        try:
            result_path = self.summarizer.extract_audio(video_path, output_path)
            self.assertTrue(os.path.exists(result_path))
            self.assertEqual(result_path, output_path)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_invalid_video_path(self):
        """Test handling of invalid video path."""
        with self.assertRaises(Exception):
            self.summarizer.extract_audio("nonexistent.mp4")

if __name__ == "__main__":
    unittest.main() 