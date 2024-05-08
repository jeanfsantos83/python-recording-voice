# pip install sounddevice | pip install scipy #
import sounddevice
from scipy.io.wavfile import write

# Set recording time #
fs=44100
second=int(input("How many seconds do you want to record? "))

print("\nRecording........\n")

# Capture the recording #
record_voice=sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()

# Save recording file #
write("recording.wav", fs, record_voice)

print("Recording finished!")
