
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
dur=5
freq=48000
recording=sd.rec(int(dur*freq),samplerate=freq,channels=2)
sd.wait()
#using scipy
write("audiofile.wav",freq,recording)


