#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Warmup task 2"""

import data

BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
