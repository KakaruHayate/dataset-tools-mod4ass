import os
import librosa
import numpy as np
import soundfile as sf

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.wav')):
            file_path = os.path.join(directory, filename)
            process_audio(file_path)

def process_audio(file_path):
    print(f"Processing {file_path}")
    y, sr = librosa.load(file_path, sr=None)

    silence_duration_samples = int(0.1 * sr)

    if len(y) < 2 * silence_duration_samples:
        print("Audio is too short, skipping.")
        return

    silence = np.zeros(silence_duration_samples)

    y_processed = np.concatenate((silence, y[silence_duration_samples:-silence_duration_samples], silence))

    base, extension = os.path.splitext(file_path)
    output_path = f"{base}_processed{extension}"
    sf.write(output_path, y_processed, sr)
    print(f"Processed audio saved to {output_path}")

directory_path = 'path/to/your/audio/files'
process_directory(directory_path)
