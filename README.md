# Video Summarizer

A Python tool that summarizes video content by extracting audio, transcribing it to text using Whisper, and generating a summary using a local Ollama model.

## Features

- Extract audio from video files
- Transcribe audio to text using OpenAI's Whisper model
- Generate concise summaries using local Ollama models
- Command-line interface for easy use
- Automatic cleanup of temporary files

## Prerequisites

- Python 3.11.11 (required for compatibility)
- FFmpeg (required for audio extraction)
- Ollama installed and running locally (https://ollama.ai)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd video-summarizer
   ```

2. Install Python 3.11.11:
   ```bash
   # On macOS using Homebrew
   brew install python@3.11
   ```

3. Set up the environment:

   ### Using uv (Recommended - Faster)
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create and activate virtual environment with Python 3.11
   uv venv -p 3.11 .venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows

   # Install dependencies using uv
   uv pip install -r requirements.txt
   ```

   ### Using pip (Alternative)
   ```bash
   # Create and activate virtual environment
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows

   # Install dependencies using pip
   pip install -r requirements.txt
   ```

4. Install and start Ollama:
   ```bash
   # Install Ollama from https://ollama.ai
   # Start the Ollama service
   ollama serve
   
   # In a new terminal, pull the Mistral model
   ollama pull mistral
   ```

## Usage

### Command Line Interface

Make sure your virtual environment is activated:
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

Basic usage:
```bash
python src/main.py path/to/video.mp4
```

Options:
- `--model MODEL`: Specify which Ollama model to use (default: mistral)
- `--no-cleanup`: Keep temporary files (optional)

Example:
```bash
python src/main.py my_video.mp4 --model mistral
```

### Python API

```python
from src.video_summarizer import VideoSummarizer

# Initialize the summarizer
summarizer = VideoSummarizer(model_name="mistral")

# Process a video
result = summarizer.process_video("path/to/video.mp4")

# Access results
print(result["transcription"])  # Full transcription
print(result["summary"])        # Summary
```

## Output

The tool provides:
1. A full transcription of the video content
2. A concise summary of the transcribed content

## Notes

- Make sure Ollama is running locally before using the tool
- The quality of transcription depends on the audio quality and the Whisper model used
- Summary quality may vary based on the content and Ollama model used
- Temporary audio files are automatically cleaned up unless `--no-cleanup` is specified
- You can use any Ollama model that supports chat completion (e.g., mistral, llama2, codellama)
- Always activate the virtual environment (`.venv`) before running the tool

## License

MIT License 