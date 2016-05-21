# -*- coding: utf-8 -*-

import os
import codecs

x = codecs.encode("The quick brown fox jumps over the lazy dog", "rot13")
codecs.decode(x, "rot13")

os.system("pause")
