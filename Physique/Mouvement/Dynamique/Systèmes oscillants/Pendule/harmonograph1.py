# -*- coding: utf-8 -*-

import os
from turtle import*
from math import*

t=0;d=100
while t<400:x=d*(sin(t)+sin(t*3.01));y=d*(sin(t*1.5)+sin(t*4.01));d*=.9999;goto(x,y);t+=.02

os.system("pause")