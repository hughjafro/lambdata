import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


VERSION = 0

ONES = np.ones(99)

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin


