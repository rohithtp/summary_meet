import os
import moviepy.editor as mp
import whisper
import ollama
from dotenv import load_dotenv

class VideoSummarizer:
    def __init__(self, model_name="mistral"):
        """Initialize the VideoSummarizer with optional model name."""
        load_dotenv()
        self.model_name = model_name
        self.whisper_model = whisper.load_model("base")
        
        # Verify Ollama model is available
        try:
            ollama.pull(self.model_name)
        except Exception as e:
            raise Exception(f"Error pulling Ollama model: {str(e)}. Make sure Ollama is running locally.")

    def extract_audio(self, video_path, output_path="extracted_audio.wav"):
        """Extract audio from video file."""
        try:
            video = mp.VideoFileClip(video_path)
            video.audio.write_audiofile(output_path)
            video.close()
            return output_path
        except Exception as e:
            raise Exception(f"Error extracting audio: {str(e)}")

    def transcribe_audio(self, audio_path):
        """Transcribe audio to text using Whisper."""
        try:
            result = self.whisper_model.transcribe(audio_path)
            return result["text"]
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")

    def summarize_text(self, text):
        """Summarize text using local Ollama model."""
        try:
            prompt = f"""Please provide a concise summary of the following text:

{text}

Keep the summary focused on the main points and key information."""
            
            response = ollama.chat(model=self.model_name, messages=[
                {
                    'role': 'system',
                    'content': 'You are a helpful assistant that summarizes text concisely.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            
            return response['message']['content']
        except Exception as e:
            raise Exception(f"Error summarizing text: {str(e)}")

    def process_video(self, video_path, cleanup=True):
        """Process video file and return summary."""
        try:
            # Extract audio
            audio_path = self.extract_audio(video_path)
            
            # Transcribe audio to text
            transcription = self.transcribe_audio(audio_path)
            
            # Summarize transcription
            summary = self.summarize_text(transcription)
            
            # Cleanup temporary files
            if cleanup and os.path.exists(audio_path):
                os.remove(audio_path)
            
            return {
                "transcription": transcription,
                "summary": summary
            }
        except Exception as e:
            raise Exception(f"Error processing video: {str(e)}") 