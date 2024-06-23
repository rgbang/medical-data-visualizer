import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
## you may have to write the full address of the file to be opened
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((0.01 * df['height']) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = 'cardio', value_vars = [
        'active',
        'alco',
        'cholesterol',
        'gluc',
        'overweight',
        'smoke'])
    # Draw the catplot with 'sns.catplot()'
    pic = sns.catplot(
        data = df_cat,
        x = 'variable',
        col = 'cardio',
        hue = 'value',
        kind = 'count')
    pic.set_axis_labels('variable', 'total')
    fig = pic.fig

    ## you may have to change the save location of the png, because not all devices save correctly
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        mask = mask,
        annot = True,
        center = 0.0,
        vmin = -0.1,
        vmax = 0.7,
        fmt = '.1f')

    ## you may have to change the save location of the png, because not all devices save correctly
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig