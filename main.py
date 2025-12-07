import pyaudio
from murf import Murf, MurfRegion

client = Murf(
    api_key="ap2_a3fa3604-d463-4e44-93ca-a3661afdceec", 
    region=MurfRegion.GLOBAL
)


SAMPLE_RATE = 24000  
CHANNELS = 1
FORMAT = pyaudio.paInt16

def play_streaming_audio():
   
    audio_stream = client.text_to_speech.stream(
        text="Hi, Rohit. I am your AI assistant.",
        voice_id="Matthew",
        model="FALCON",
        multi_native_locale="en-US",
        sample_rate=SAMPLE_RATE,
        format="PCM"
    )

    
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, output=True)

    try:
        print("Starting audio playback...")
        for chunk in audio_stream:
            if chunk: 
                stream.write(chunk)
    except Exception as e:
        print(f"Error during streaming: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        print("Audio streaming and playback complete!")

if __name__ == "__main__":
    play_streaming_audio()

