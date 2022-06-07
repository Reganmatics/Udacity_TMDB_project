__author__ = "Reganmatics"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file = 'tmdb-movies.csv'
movie_df = pd.read_csv(file)



def feature_info_plot(col_name):
    #data_setup
    Title = f"yearly {col_name}"
    temp_data = df.groupby('release_year')[col_name].sum()
    
    #plot_face
    plt.figure(figsize=(15,5))
    plt.plot(temp_data)
    plt.title(Title)
    plt.xlabel('year')
    plt.ylabel(col_name)
    plt.show()
    
    
def high_and_low(col_name):
    #for highest earned profit
    high= df[col_name].idxmax()
    high_details=pd.DataFrame(df.loc[high])
    
    #for lowest earned profit
    low= df[col_name].idxmin()
    low_details=pd.DataFrame(df.loc[low])
    
    #collectin data in one place
    info=pd.concat([high_details, low_details], axis=1)
    
    return info


def plot_best_fit(col_name):
    #data setup
    Title = f"yearly {col_name}"
    temp_data = df.groupby('release_year')[col_name].sum()
    pds = pd.Series(temp_data)
    years = np.array(pds.index.values)
    yearly_values = np.array([pds[i] for i in years])
    x,y = years, yearly_values
    
    #gradient and intercept
    m,c = np.polyfit(x, y, 1)
    
    #plot of best fit
    plt.figure(figsize=(15,5))
    plt.plot(x,y,'*')
    plt.plot(x, m*x + c)
    plt.title(Title)
    plt.xlabel('year')
    plt.ylabel(col_name)
    plt.show()
    

def corr_plot(col1, col2):
    df.plot(x=col1, y=col2, kind='scatter')