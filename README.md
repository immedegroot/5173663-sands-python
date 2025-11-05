# Introduction
This project shows how to generate two basic signals and apply time domain operations using python, numpy and matplotlib. 

# Files:

#### signals.py contains two signals:
- generate_sine_wave(frequency, duration, sample_rate): creates a sine wave signal
- generate_square_wave(frequency, duration, sample_rate): creates a square wave signal

it also contains time domain operations:
- time_shift(signal, shift_samples): shifts a sigal forward or backward in time
- time_scale(signal, scale_factor): stretches or compresses a signal in time

it also contains one frequency domain function:
- fourier_series_square(t, period, n_terms=10, amplitude=1.0): approximates a square wave, showing how a periodic dquare wave can be built from summed sine waves

#### a test.py file to test the functions

#### run.py file 
1. gerenates a 5hz sine and square wave
2. shifts the sine wave in time b 0.2 s
3. scales the square wave by 0.5x
4. computes FFT spectra of both signals
5. plots original and shifted/scaled waves and their frequency spectra

# how to use
- make sure python, numpy and maplotlib are installed
- run the signals: signals.py
- run the tests: test.py
- run.py will open plots of the original and scaled/shifted waves and the fourier series and spectra




