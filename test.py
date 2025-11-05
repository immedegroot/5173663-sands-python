"""
test.py
--------
Automated tests for the Signal Operations Project.

This script verifies the correctness of signal generation and manipulation functions
from signals.py. It performs numerical checks (no plotting) for:

1. Sine wave generation
2. Square wave generation
3. Time shifting
4. Time scaling
5. Fourier series square-wave approximation

Each test prints a success message if passed and raises an AssertionError otherwise.
"""

import numpy as np
from signals import (
    generate_sine_wave,
    generate_square_wave,
    time_shift,
    time_scale,
    fourier_series_square,
)


def test_generate_sine_wave():
    """
    Test the sine wave generator for expected frequency and amplitude behavior.

    Checks:
    - The signal amplitude stays within [-1, 1].
    - The estimated frequency (from zero crossings) is close to the target frequency.
    """
    fs = 1000        # sampling rate [Hz]
    freq = 5         # signal frequency [Hz]
    dur = 1.0        # signal duration [s]

    sine = generate_sine_wave(freq, dur, fs)
    t = np.arange(len(sine)) / fs

  
    assert np.all(np.abs(sine) <= 1.0 + 1e-10), "Sine amplitude exceeds ±1"

   
    zero_crossings = np.where(np.diff(np.signbit(sine)))[0]
    est_freq = len(zero_crossings) / (2 * dur)
    assert np.isclose(est_freq, freq, atol=0.5), f"Sine frequency off: {est_freq} Hz"

    print("generate_sine_wave passed")


def test_generate_square_wave():
    """
    Test the square wave generator for expected amplitude levels.

    Checks:
    - The waveform only contains values close to -1, 0, or +1.
    """
    fs = 1000
    freq = 5
    dur = 1.0
    square = generate_square_wave(freq, dur, fs)

    unique_values = np.unique(np.round(square, 2))
    assert set(unique_values).issubset({-1.0, 0.0, 1.0}), f"Unexpected values: {unique_values}"

    print("generate_square_wave passed")


def test_time_shift():
    """
    Test the time_shift function for both positive and negative shifts.

    Checks:
    - Positive shift adds zeros at the start and truncates the end.
    - Negative shift adds zeros at the end and truncates the beginning.
    """
    sig = np.array([1, 2, 3, 4, 5])

    
    shifted = time_shift(sig, 2)
    assert np.allclose(shifted[:2], 0), "Positive shift should start with zeros"
    assert np.allclose(shifted[2:], sig[:-2]), "Positive shift misaligned"

    
    shifted_back = time_shift(sig, -2)
    assert np.allclose(shifted_back[-2:], 0), "Negative shift should end with zeros"
    print("time_shift passed")


def test_time_scale():
    """
    Test the time_scale function for signal length changes.

    Checks:
    - Compression (<1.0) decreases signal length.
    - Stretching (>1.0) increases signal length.
    """
    sig = np.arange(10)

    
    scaled = time_scale(sig, 0.5)
    assert len(scaled) < len(sig), "Compression should reduce signal length"

    
    scaled = time_scale(sig, 2.0)
    assert len(scaled) > len(sig), "Stretching should increase signal length"

    print("time_scale passed")


def test_fourier_series_square():
    """
    Test the Fourier series approximation for a square wave.

    Checks:
    - The mean absolute error between the true and approximated square wave is small.
    """
    fs = 1000
    f0 = 5
    dur = 1.0
    t = np.linspace(0, dur, int(fs * dur), endpoint=False)
    period = 1.0 / f0

    square_true = generate_square_wave(f0, dur, fs)
    square_fs_15 = fourier_series_square(t, period, n_terms=15, amplitude=1.0)

   
    error = np.mean(np.abs(square_true - square_fs_15))
    assert error < 0.3, f"Fourier series approximation too poor (error={error:.3f})"

    print("fourier_series_square passed")


def main():
    """
    Run all tests sequentially and print summary.
    """
    test_generate_sine_wave()
    test_generate_square_wave()
    test_time_shift()
    test_time_scale()
    test_fourier_series_square()

    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    main()