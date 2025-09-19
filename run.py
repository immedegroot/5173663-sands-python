import matplotlib.pyplot as plt
from signals import generate_sine_wave

# Parameters
frequency = 5
duration = 2
sample_rate = 100

# Generate sine wave
signal = generate_sine_wave(frequency, duration, sample_rate)

# Plot the sine wave
plt.plot(signal)
plt.title('Generated Sine Wave (5 Hz)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
