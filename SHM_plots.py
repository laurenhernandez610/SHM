from matplotlib.widgets import MultiCursor
import matplotlib.pyplot as plt
import numpy as np

# This script sets up plots of oscillations over time

fig = plt.figure()
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)
t = np.arange(0.0, 3.0, 0.01)
ax1 = fig.add_subplot(311)
ax1.plot(t, np.sin(0.9*np.pi*t))
ax2.plot(t, np.sin(4*np.pi*t))
ax3.plot(t, np.sin(8*np.pi*t))

multi = MultiCursor(fig.canvas, (ax1, ax2, ax3), color='y', lw=1,
                    horizOn=True, vertOn=True)

st = fig.suptitle('Simple Harmonic Oscillations with Varying Parameters')

plt.show()
