import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

fig = plt.figure()

class main():
    def __initial__(self):
        self.amplitude = 1
        self.time_period = 1
        self.damp_constant = 1
        self.mass = 1

    def update_amplitude(self, event):
        if float(self.amplitude_box.text) > 0:
            self.amplitude = float(self.amplitude_box.text)
        else:
            self.amplitude = 1 

    def update_time_period(self, event):
        if float(self.time_period_box.text) > 0:
            self.time_period = float(self.time_period_box.text)
        else:
            self.time_period = 1

    def update_damp_constant(self, event):
        if float(self.damp_constant_box.text) > 0:
            self.damp_constant = float(self.damp_constant_box.text)
        else:
            self.damp_constant = 1

    def update_mass(self, event):
        if float(self.mass_box.text) > 0:
            self.mass = float(self.mass_box.text)
        else:
            self.mass = 1

    def initial(self):
        ball_center = 0, 5
        ball = self.p1.plot(0, 5, 'ro')
        return ball

    def animate(self, i):
        amplitude = self.amplitude
        t = self.time_period
        b = self.damp_constant
        m = self.mass

        w = 2 * np.pi / t
        w_ = abs((w ** 2 - (b ** 2 / (4 * m))) ** 0.5)

        x = amplitude * np.exp(-b * i/ (2 * m * 50)) * np.cos(w_ * i / 50)

        ball_center = x, 5
        ball = self.p1.plot(x, 5, 'ro')
        return ball

    def go(self, event): 
        amplitude = self.amplitude
        t = self.time_period
        b = self.damp_constant
        m = self.mass

        w = 2 * np.pi / t
        w_ = (w ** 2 - (b ** 2 / (4 * m))) ** 0.5

        fig.clf()


        back_box = plt.axes([0.8, 0.9, 0.07, 0.075])
        self.back_button = Button(back_box, "Back")
        self.back_button.on_clicked(self.back)
        self.p1 = fig.add_subplot(211)
        self.p2 = fig.add_subplot(212)

        self.p1.set_xlim(-amplitude - 3, amplitude + 3)
        self.p1.set_ylim(0, 10)
        self.p1.get_yaxis().set_visible(False)
        self.p1.plot([-amplitude, amplitude], [5]*2)

        self.p2.set_ylim(-amplitude, amplitude)
        self.p2.set_xlim(0, 10*t)
        self.p2.plot([0, 10*t], [0]*2, 'y')

        self.p2.set_xlabel('Time (seconds)')
        self.p2.set_ylabel('Displacement (meters)')

        x = np.arange(0, 10 * t, 0.01)
        y = amplitude * np.exp(-b / (2 * m) * x) * np.cos(w_ * x)
        line, = self.p2.plot(x, y)

        self.anim = animation.FuncAnimation(fig, self.animate,
                                        init_func=self.init,
                                        interval=20,
                                        blit=True)

        plt.draw()


    def init_page(self):

        fig.text(0.2, 0.8, 'Simple Harmonic Motion: Simulation Generator', fontsize = 45)

        amplitude_box_loc = plt.axes([0.4, 0.5, 0.2, 0.075])
        self.amplitude_box = TextBox(amplitude_box_loc, 'Amplitude (A)', initial=str(self.amplitude))
        time_period_box_loc = plt.axes([0.4, 0.4, 0.2, 0.075])
        self.time_period_box = TextBox(time_period_box_loc, 'Time Period (T)', initial=str(self.time_period))
        damp_constant_box_loc = plt.axes([0.4, 0.3, 0.2, 0.075])
        self.damp_constant_box = TextBox(damp_constant_box_loc, 'Damping Constant (k)', initial=str(self.damp_constant))
        mass_box_loc = plt.axes([0.4, 0.2, 0.2, 0.075])
        self.mass_box = TextBox(mass_box_loc, 'Mass of ball (m)', initial=str(self.mass))

        bbox1 = plt.axes([0.45, 0.1, 0.1, 0.075])
        self.button1 = Button(bbox1, "GO!")

        self.amp_box.on_submit(self.update_amplitude)
        self.tp_box.on_submit(self.update_time_period)
        self.dp_box.on_submit(self.update_damp_constant)
        self.mass_box.on_submit(self.update_mass)
        self.button1.on_clicked(self.go)
        plt.draw()

    def back(self, event):
        fig.clear()
        try:
            self.anim.event_source.stop()
        except:
            None
        return self.init_page()

main().init_page()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()


