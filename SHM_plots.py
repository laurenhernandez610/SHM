from matplotlib.widgets import MultiCursor
import matplotlib.pyplot as plt
import numpy as np

# -----This script sets up plots of oscillations over time-----
# Alternate, more concise way to plot: 
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=False)

fig = plt.figure()
t = np.arange(0.0, 2.0, 0.01)

ax1 = fig.add_subplot(311)
ax1.plot(t, np.sin(0.9*np.pi*t))
ax1.set_title("ax1", fontsize=9)

ax2 = fig.add_subplot(312)
ax2.plot(t, np.sin(4*np.pi*t))
ax2.set_title("ax2", fontsize=9)

ax3 = fig.add_subplot(313)
ax3.plot(t, np.sin(8*np.pi*t))
ax3.set_title("ax3", fontsize=9)

multi = MultiCursor(fig.canvas, (ax1, ax2, ax3), color='y', lw=1,
                    horizOn=True, vertOn=True)

fig.tight_layout()

st = fig.suptitle('Simple Harmonic Oscillations with Varying Parameters', fontsize=10)
st.set_y(0.95)
fig.subplots_adjust(top=0.85)

plt.show()
