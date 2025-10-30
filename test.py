import numpy as np
from signals import generate_sine_wave, time_shift, time_scale
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