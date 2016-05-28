# -*- coding: utf-8 -*-

import os

# Random Spiral IFS Fractals
# FB - 20130928

import math
import random
from PIL import Image

imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
maxIt = imgx * imgy
n = random.randint(2, 9)
a = 2.0 * math.pi / n
t = 2.0 * math.pi * random.random()  # rotation angle of central copy
ts = math.sin(t)
tc = math.cos(t)
# scale factor of outmost copies on the spiral arms
r1 = 0.2 * random.random() + 0.1
r0 = 1.0 - r1  # scale factor of central copy
p0 = r0 ** 2.0 / (n * r1 ** 2.0 + r0 ** 2.0)  # probability of central copy
x = 0.0
y = 0.0

for i in range(maxIt):
    if random.random() < p0:  # central copy
        x *= r0
        y *= r0  # scaling
        # rotation
        h = x * tc - y * ts
        y = x * ts + y * tc
        x = h
    else:  # outmost copies on the spiral arms
        k = random.randint(0, n - 1)  # select an arm
        c = k * a  # angle
        # scaling and translation
        x = x * r1 + math.cos(c)
        y = y * r1 + math.sin(c)
    kx = int((x + 2.0) / 4.0 * (imgx - 1))
    ky = int((y + 2.0) / 4.0 * (imgy - 1))
    pixels[kx, ky] = (255, 255, 255)
image.save("RandomSpiralIFSFractal.png", "PNG")

os.system("pause")
