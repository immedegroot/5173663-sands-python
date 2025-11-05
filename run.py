"""
This script demonstrates:
1. Generating a sine and a square wave.
2. Applying time-domain operations:
   - Time shift (on the sine wave)
   - Time scale (on the square wave)
3. Computing and plotting their Fourier spectra.
4. Comparing a generated square wave to its
   analytical Fourier Series approximation.

Requirements:
- signals.py must define:
  generate_sine_wave(), generate_square_wave(),
  time_shift(), time_scale(), fourier_series_square()
"""

import matplotlib.pyplot as plt
import numpy as np


    generate_sine_wave,
    generate_square_wave,
    time_shift,
    time_scale,
    fourier_series_square
)


def compute_fft(x, fs):
    """
    Compute the single-sided amplitude spectrum of a real-valued signal.

    Parameters
    ----------
    x : np.ndarray
        Input signal (time-domain samples)
    fs : float
        Sampling rate in Hz

    Returns
    -------
    f : np.ndarray
        Frequency axis (Hz)
    A : np.ndarray
        Amplitude spectrum (normalized)
    """
    X = np.fft.rfft(x) 
    f = np.fft.rfftfreq(len(x), 1 / fs)
    A = np.abs(X) / len(x)
    return f, A


def main():
    """
    Run the complete demonstration:
    - Generate sine and square waves
    - Apply time shift and time scaling
    - Plot time-domain and frequency-domain results
    - Compare generated square wave to its Fourier Series approximation
    """

    
    fs = 500           # Sampling rate [Hz]
    dur = 1.0          # Signal duration [s]
    freq = 5           # Signal frequency [Hz]

    
    sine = generate_sine_wave(freq, dur, fs)
    square = generate_square_wave(freq, dur, fs)

   
    sine_shifted = time_shift(sine, int(0.2 * fs))   # shift by 0.2 s
    square_scaled = time_scale(square, 0.5)          # compress by factor 0.5

    
    t = np.arange(len(sine)) / fs
    ts = np.arange(len(square_scaled)) / fs

    
    plt.figure()
    plt.plot(t, sine, label='Sine')
    plt.plot(t, sine_shifted, '--', label='Sine shifted')
    plt.legend(); plt.grid(); plt.title('Sine Wave (original & shifted)')
    plt.xlabel('Time [s]'); plt.ylabel('Amplitude')

    plt.figure()
    plt.plot(t, square, label='Square')
    plt.plot(ts, square_scaled, ':', label='Square scaled')
    plt.legend(); plt.grid(); plt.title('Square Wave (original & scaled)')
    plt.xlabel('Time [s]'); plt.ylabel('Amplitude')

   
    f1, A1 = compute_fft(sine, fs)
    f2, A2 = compute_fft(square, fs)

    plt.figure()
    plt.plot(f1, A1, label='Sine spectrum')
    plt.plot(f2, A2, label='Square spectrum')
    plt.xlim(0, 50)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.legend(); plt.grid(); plt.title('Fourier Spectra')

    
    series = fourier_series_square(t, period=1 / freq, n_terms=15, amplitude=1.0)

    plt.figure()
    plt.plot(t, square, label='Generated Square wave')
    plt.plot(t, series, '--', label='Fourier Series (15 odd harmonics)')
    plt.legend(); plt.grid(); plt.title('Square Wave vs Fourier Series Approximation')
    plt.xlabel('Time [s]'); plt.ylabel('Amplitude')

   
    plt.show()


if __name__ == "__main__":
    main()