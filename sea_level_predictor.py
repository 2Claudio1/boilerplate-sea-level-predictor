import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('epa-sea-level.csv')


    ##### Create scatter plot #####
    # Create a scatter plot using the Year column as the x-axis 
    # and the CSIRO Adjusted Sea Level column as the y-axis.
    x_col = 'Year'
    y_col = 'CSIRO Adjusted Sea Level'
    
    fig, ax = plt.subplots(figsize=(12, 7))
    plt.scatter(df[x_col], df[y_col])


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()