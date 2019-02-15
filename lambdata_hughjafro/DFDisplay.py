
'''
The DFDispaly class is a useful display helper
'''

Class DFDispaly(object):
    def __init__(self)
    #Initialize the function
    self.randrange()
    self.unlimited_columns()
    self.unlimited_rows()
    
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
