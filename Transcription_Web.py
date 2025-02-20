import streamlit as st
import numpy as np
import wave
import time
import whisper
import torch
torch.classes.__path__ = []
st.title("🎤 Simple Audio Recorder with Streamlit")

# Audio input widget
audio_file = st.audio_input("Record your voice")

if audio_file:
    file_name = f"recording_{int(time.time())}.wav"
    
    # Save the audio file
    with open(file_name, "wb") as f:
        f.write(audio_file.getvalue())
    
    st.success(f"Recording saved as {file_name}")

    # Provide a download button
    with open(file_name, "rb") as f:
        st.download_button("Download Recording", f, file_name, "audio/wav")

    # Whisper Transcription Button
    if st.button("Recording to Text"):
        model = whisper.load_model("base")  # Load a Whisper model
        result = model.transcribe(file_name)
        st.text_area("Transcribed Text:", result["text"], height=200)
