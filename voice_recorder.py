import sounddevice as sd
import numpy as np
import lameenc as l


fs = 44100
channels = 1
chunks = []


def callback(indata, frames, time, status):
    chunks.append(indata.copy())


def save_as_mp3(recording, filename, fs, channels):
    rec_int = (recording*32767).astype(np.int16) #int raw bytes for lameenc

    enc = l.Encoder()
    enc.set_bit_rate(128)
    enc.set_in_sample_rate(fs)
    enc.set_channels(channels)
    enc.set_quality(2) 

    mp3_data = enc.encode(rec_int.flatten().tobytes())
    mp3_data += enc.flush()

    if not filename.endswith('.mp3'):
        filename += '.mp3'
    with open(filename, 'wb') as f:
        f.write(mp3_data)


print("Press 'Enter' to start recording...")
input()

stream = sd.InputStream(samplerate=fs, channels=channels, dtype='float32', callback=callback)
with stream:
    print("Recording, press 'Enter' to stop recording...")
    input()


recording = np.concatenate(chunks, axis=0).astype(np.float32) #float numpy array



file_name = input("What would you like to call this recording (___.mp3): ") 
save_as_mp3(recording, file_name, fs, channels)