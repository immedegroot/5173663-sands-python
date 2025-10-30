import numpy as np
from signals import generate_sine_wave, generate_square_wave, time_shift, time_scale, fourier_series_square
import matplotlib.pyplot as plt

fs = 1000
sig = generate_sine_wave(5, 1, fs)
shifted = time_shift(sig, 100)
scaled = time_scale(sig, 0.5)

plt.plot(sig, label="Original")
plt.plot(shifted, label="Shifted")
plt.plot(scaled, label="Scaled")
plt.legend()
plt.show()

f0 = 5.0 
duration = 1.0
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
period = 1.0 / f0


square_true = generate_square_wave(f0, duration, fs)
square_fs_5  = fourier_series_square(t, period, n_terms=5,  amplitude=1.0)
square_fs_15 = fourier_series_square(t, period, n_terms=15, amplitude=1.0)


plt.figure(figsize=(10, 4))
plt.plot(t, square_true, label="Square (true)")
plt.plot(t, square_fs_5,  "--", label="Fourier series N=5")
plt.plot(t, square_fs_15, ":",  label="Fourier series N=15")
plt.xlim(0, 3 / f0)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Square wave: true vs Fourier series approximation")
plt.legend()
plt.tight_layout()

plt.show()