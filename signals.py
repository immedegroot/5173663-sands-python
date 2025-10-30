import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)
    """ 
    Generate a sine wave signal
    Frequency: frequency of the sine wave in Hz
    Duration: duration of signla in seconds
    Sample rate: number of samples per second
    Output: a sine wave function

    """

def generate_square_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sign(np.sin(2 * np.pi * frequency * t))
    """
    Generate a square wave signal
    Frequency: frequency of the sine wave in Hz
    Duration: duration of signla in seconds
    Sample rate: number of samples per second
    Output: a square wave funtion

    """

def time_shift(signal, shift_samples):
    """
    Shift a signal left or right in time.
    Positive shift -> delay (move right)
    Negative shift -> advance (move left)
    """
    if shift_samples > 0:
        shifted = np.concatenate((np.zeros(shift_samples), signal[:-shift_samples]))
    elif shift_samples < 0:
        shifted = np.concatenate((signal[-shift_samples:], np.zeros(-shift_samples)))
    else:
        shifted = signal.copy()
    return shifted

def time_scale(signal, scale_factor):
    """
    Scale a signal in time.
    >1.0 -> slow down (stretch)
    <1.0 -> speed up (compress)
    """
    if scale_factor <= 0:
        raise ValueError("scale_factor must be positive")
    indices = np.arange(0, len(signal), 1 / scale_factor)
    indices = indices[indices < len(signal)].astype(int)
    return signal[indices]

def fourier_series_square(t, period, n_terms=10, amplitude=1.0):
    """
    Approximate a square wave using its sine Fourier series with N odd harmonics.
    y(t) ≈ (4A/π) * Σ_{k=1..n_terms} sin[(2k-1) * ω0 * t] / (2k-1)
    """
    w0 = 2 * np.pi / period
    y = np.zeros_like(t, dtype=float)
    for k in range(1, n_terms + 1):
        n = 2 * k - 1  # odd harmonic index: 1,3,5,...
        y += np.sin(n * w0 * t) / n
    return (4 * amplitude / np.pi) * y