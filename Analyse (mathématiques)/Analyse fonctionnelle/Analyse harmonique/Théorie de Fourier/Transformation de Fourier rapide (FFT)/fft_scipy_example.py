# -*- coding: utf-8 -*-

import os
import scipy
from scipy.fftpack import fft, fftfreq

npts = 4000
nplot = npts / 10
t = linspace(0, 120, npts)


def acc(t): return 10 * sin(2 * pi * 2.0 * t) + \
    5 * sin(2 * pi * 8.0 * t) + 2 * rand(npts)

signal = acc(t)

FFT = abs(fft(signal))
freqs = fftfreq(npts, t[1] - t[0])

subplot(211)
plot(t[:nplot], signal[:nplot])
subplot(212)
plot(freqs, 20 * log10(FFT), ',')
show()

os.system("pause")
