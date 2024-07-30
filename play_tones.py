from struct import pack
from time import sleep

import pyaudio
import numpy as np

pyaud = pyaudio.PyAudio()
Fs = 26500

stream = pyaud.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=Fs,
                        output=True)
def playOnce(freq, duration):
    nsamples = int(Fs * duration)

    signal = np.arange(nsamples)
    signal = np.sin(2 * np.pi * freq * signal / Fs)



    out = pack("%df" % len(signal), *(signal))
    stream.write(out)



def playRange(startFreq,endFreq, subdivisions,duration):
    for i in range(subdivisions):
        print(startFreq + ((i * (endFreq - startFreq) / (subdivisions - 1))))
        playOnce(startFreq+((i*(endFreq-startFreq)/(subdivisions-1))),duration)

playRange(0,8000,161,1)
stream.stop_stream()
stream.close()
pyaud.terminate()

