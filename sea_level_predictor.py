import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    ##### Read data from file #####
    # Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('epa-sea-level.csv')


    ##### Create scatter plot #####
    # Create a scatter plot using the Year column as the x-axis 
    # and the CSIRO Adjusted Sea Level column as the y-axis.
    x_col = 'Year'
    y_col = 'CSIRO Adjusted Sea Level'
    
    fig, ax = plt.subplots(figsize=(12, 7))
    plt.scatter(df[x_col], df[y_col])


    ##### Create first line of best fit #####
    # Generate a range of years from the minimum year in the dataset to 2050
    first_pred_years = pd.Series(range(df[x_col].min(), 2051))
    
    # Calculate the slope and y-intercept for the first line of best fit, using the linregress function from scipy.stats. 
    # This line will predict sea level rise until 2050
    first_slope, first_intercept, first_r, first_p, first_se = linregress(df[x_col], df[y_col])
    
    # Plot the first line of best fit on the scatter plot. # m(slope)*x+b(intercept)
    plt.plot(first_pred_years,  first_slope * first_pred_years + first_intercept, 'g-')


    ##### Create second line of best fit #####
    # Filter the data to include only the years from 2000 onwards.
    recent_sea_level_data = df[df[x_col] >= 2000]
    
    # Calculate the slope and y-intercept for the second line of best fit.
    # This line will predict sea level rise until 2050 based on data from 2000 onward.
    second_slope, second_intercept, second_r, second_p, second_se = linregress(recent_sea_level_data[x_col], recent_sea_level_data[y_col])
    
    # Plot the first line of best fit on the scatter plot.
    second_pred_years = range(2000, 2051)
    plt.plot(second_pred_years, second_slope * pd.Series(second_pred_years) + second_intercept, 'r--')


    ##### Add labels and title #####
    # Set the x-axis label, y-axis label, and plot title.
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()