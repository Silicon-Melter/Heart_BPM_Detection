import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks
import wave
import sys

audioname = 'Test1.wav'
spf = wave.open(audioname, "r")
# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()
# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

Time = np.linspace(0, len(signal) / fs, num=len(signal))

ab_signal = np.abs(signal)
signal_filtered = savgol_filter(ab_signal, 4999, 3)

peaks2, _ = find_peaks(signal_filtered, prominence=1000) 

print(len(peaks2))

plt.subplot(2, 2, 1)
plt.plot(signal, 'r'); plt.title("1st")
plt.subplot(2, 2, 2)
plt.plot(ab_signal, 'b'); plt.title("2nd")
plt.subplot(2, 2, 3)
plt.plot(signal_filtered, 'g'); plt.title("3rd")
plt.subplot(2, 2, 4)
plt.plot(peaks2, signal_filtered[peaks2], "ob")
plt.plot(signal_filtered, 'g')
plt.title("4th")
plt.show()