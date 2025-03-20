import argparse
import os
from video_summarizer import VideoSummarizer

def main():
    parser = argparse.ArgumentParser(description="Summarize video content using AI")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("--model", default="mistral", help="Ollama model name (default: mistral)")
    parser.add_argument("--no-cleanup", action="store_true", help="Don't remove temporary files")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.video_path):
        print(f"Error: Video file not found at {args.video_path}")
        return
    
    try:
        summarizer = VideoSummarizer(model_name=args.model)
        result = summarizer.process_video(args.video_path, cleanup=not args.no_cleanup)
        
        print("\n=== Transcription ===")
        print(result["transcription"])
        print("\n=== Summary ===")
        print(result["summary"])
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 