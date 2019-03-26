# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:32:08 2019

@author: Sebastian Duesing
"""

import numpy as np
import PyMieScatt as ps

diameter = np.array([100, 200, 300])
wavelengths = np.array([355, 532, 1064])

for d in diameter:
    for w in wavelengths:
        result = ps.MieQ(1.53 + 0.015j, d, w, asDict=True)
        print(result)
        # Qback = result['Qback']
        # Qabs = result['Qabs']
        # Qsca = result['Qsca']
        # Qext = result['Qext']



