from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Generate a test signal
# a 2 Vrms sine wave whose frequency is slowly modulated around 3kHz,
# corrupted by white noise of exponentially decreasing magnitude
# sampled at 10 kHz.

fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2
time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
noise *= np.exp(-time/5)
x = carrier + noise

# Compute and plot the spectrogram.

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

from scipy.io.wavfile import read,write
from pylab import plot,show,subplot,specgram

# Open the Homer Simpson voice: "Ummm, Crumbled up cookie things."
# from http://www.thesoundarchive.com/simpsons/homer/mcrumble.wav
rate,data = read('Whistling.wav') # reading

subplot(411)
plot(range(len(data)),data)
subplot(412)
# NFFT is the number of data points used in each block for the FFT
# and noverlap is the number of points of overlap between blocks
specgram(data, NFFT=128, noverlap=0) # small window
subplot(413)
specgram(data, NFFT=512, noverlap=0)
subplot(414)
specgram(data, NFFT=1024, noverlap=0) # big window

show()


###


# import the libraries
import matplotlib.pyplot as plot
import numpy as np

 # Define the list of frequencies
frequencies = np.arange(5,105,5)

 # Sampling Frequency
samplingFrequency   = 400

 # Create two ndarrays
s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal

# Start Value of the sample
start   = 1

# Stop Value of the sample
stop = samplingFrequency+1
for frequency in frequencies:
     sub1 = np.arange(start, stop, 1)

 # Signal - Sine wave with varying frequency + Noise
sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))
s1 = np.append(s1, sub1)
s2 = np.append(s2, sub2)
start = stop+1
stop = start+samplingFrequency

 # Plot the signal
plot.subplot(211)
plot.plot(s1,s2)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

# Plot the spectrogram
plot.subplot(212)
powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show()


# import the libraries

import matplotlib.pyplot as plot

import numpy as np


# Define the list of frequencies

frequencies         = np.arange(5,105,5)


# Sampling Frequency

samplingFrequency   = 400


# Create two ndarrays

s1 = np.empty([0]) # For samples

s2 = np.empty([0]) # For signal


# Start Value of the sample

start   = 1


# Stop Value of the sample

stop    = samplingFrequency+1


for frequency in frequencies:

    sub1 = np.arange(start, stop, 1)



    # Signal - Sine wave with varying frequency + Noise

    sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))



    s1      = np.append(s1, sub1)

    s2      = np.append(s2, sub2)



    start   = stop+1

    stop    = start+samplingFrequency


# Plot the signal

plot.subplot(211)

plot.plot(s1,s2)

plot.xlabel('Sample')

plot.ylabel('Amplitude')


# Plot the spectrogram

plot.subplot(212)

powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

plot.show()
