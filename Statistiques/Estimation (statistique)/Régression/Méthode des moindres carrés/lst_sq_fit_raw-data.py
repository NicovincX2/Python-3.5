# -*- coding: utf-8 -*-

import os
import numpy

raw_data = """\
3.1905781584582433,0.028208609537968457
4.346895074946466,0.007160804747670053
5.374732334047101,0.0046962988461934805
8.201284796573875,0.0004614473299618756
10.899357601713055,0.00005038370219939726
16.295503211991434,4.377451812785309e-7
21.82012847965739,3.0799922117601088e-9
32.48394004282656,1.524776208284536e-13
43.53319057815846,5.5012073588707224e-18"""

data = []
for line in raw_data.splitlines():
    words = line.split(',')
    data.append(map(float,words))
data = array(data)

title("Raw Data")
xlabel("Distance")
plot(data[:,0],data[:,1],'bo')

title("Raw Data")
xlabel("Distance")
semilogy(data[:,0],data[:,1],'bo')

params = polyfit(data[:,0],log(data[:,1]),1)
a = params[0]
A = exp(params[1])

x = linspace(1,45)
title("Raw Data")
xlabel("Distance")
semilogy(data[:,0],data[:,1],'bo')
semilogy(x,A*exp(a*x),'b-')

os.system("pause")