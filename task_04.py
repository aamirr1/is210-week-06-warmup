#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Warmup task 4"""

def process_data(data):
    """ This function will returns sum of the data and the average of the data
    Args:
        data (mixed): This will include list of numbers 
    Returns:
        tuple: this will include the total sum of the data and the average
               of the data
    Example:
        >>> process_data([1, 2, 3])
             (6, 2.0)
    """
    
    totalsum = 0
    for mynum in data:
        totalsum += mynum
    myavg = (totalsum / float(len(data)))

    return (totalsum, myavg)
