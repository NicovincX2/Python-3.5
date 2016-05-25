# -*- coding: utf-8 -*-

import os

from pylab import*
from numpy import*
i=99
X,Y=mgrid[-2:2:999j,-2:2:999j]
C=Z=X*1j+Y
while i:X[(abs(Z)>2)]=i;Z=Z*Z+C;i-=1
show(imshow(X))

os.system("pause")