import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

VERSION = 0

ONES = np.ones(99)

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

def unlimited_columns(self):
        '''
        Helper function to display unlimited columns.
        When dealing with dataframes with many columns, this function will allow all columns to be viewed.
        
        Using transpose or df.T, is a useful operation when a viewing a dataframe with many features. 
        '''
        print("pd.set_option('display.max_columns', None)")
        
def unlimited_rows(self):
        '''
        Helper function to display unlimited rows.
        
        This function will allow all rows to be viewed.
        '''
        print("pd.set_option('display.max_rows', None)")
